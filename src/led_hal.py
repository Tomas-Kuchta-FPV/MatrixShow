from .config import matrix, MQTT_PYTHON_ZIGBEE2MQTT_TOPIC, MQTT_ENABLED, DEBUG_PRINTS, SONOFF_ENABLED, SONOFF_MS
from time import sleep

from .Protocols import Sonoff_DIY_mode, mqtt

import json
import os
import tempfile
import fcntl


def init_leds():
    global XY, LED_STATE
    width = len(matrix[0])
    height = len(matrix)
    XY = (width, height)  # X = columns, Y = rows
    # initialize LED_STATE with defaults (OFF)
    LED_STATE = {}
    for y in range(height):
        for x in range(width):
            LED_STATE[(x, y)] = {
                "state": "OFF",
                "x": x,
                "y": y,
                "color_temp": None,
                "brightness": 0,
                "device": matrix[y][x],
            }
    # try to load persisted state and merge (persisted wins for existing bulbs)
    persisted = _load_state_from_disk()
    if persisted:
        for (px, py), val in persisted.items():
            # only accept values that fit in current matrix
            if 0 <= py < height and 0 <= px < width:
                LED_STATE[(px, py)] = val
        # ensure device names are current
        for (x, y), entry in LED_STATE.items():
            entry["device"] = matrix[y][x]
    print(f"LEDs initialized with dimensions: {XY}")
    return


def set_bulb_on_ct(x, y, color_temp, brightness):
    """Set bulb at position (x, y) to given temperature and brightness.
    x: column index (0-based)
    y: row index (0-based)
    color_temp: color temperature (0-100) 0 is the coolest, 100 is the warmest
    brightness: brightness level (1-100)
    """

    # bounds check
    if brightness < 1 or brightness > 100:
        raise ValueError(f"brightness is set {brightness} and must be between 1 and 100")
    if color_temp < 0 or color_temp > 100: # 0 is the coolest, 100 is the warmest
        raise ValueError(f"color_temp is set {color_temp_sonoff} and must be between 0 and 100")
    if y < 0 or y >= len(matrix) or x < 0 or x >= len(matrix[0]):
        raise IndexError(f"x,y {x},{y} out of range")
    
    device = matrix[y][x]

    if DEBUG_PRINTS:
        print(f"DEBUG_PRINTS: set_bulb_on_ct({x}, {y}, {color_temp}, {brightness})")

    if MQTT_ENABLED is True:
        brightness_mqtt = map_range(brightness, 0, 100, 0, 254)
        color_temp_mqtt = map_range(color_temp, 0, 100, 153, 500)
        payload = {"color_temp": color_temp_mqtt, "brightness": brightness_mqtt, "state": "ON"}

        topic = MQTT_PYTHON_ZIGBEE2MQTT_TOPIC.format(DeviceName=device)
        mqtt.send(topic, payload)

    if SONOFF_ENABLED is True:
        color_temp_sonoff = map_range(color_temp, 0, 100, 100, 0)
        Sonoff_DIY_mode.color_temp(device, brightness, color_temp_sonoff, SONOFF_MS)

    # persist state for future reference
    LED_STATE[(x, y)] = {
        "state": "ON",
        "x": x,
        "y": y,
        "color_temp": color_temp,
        "brightness": brightness,
        "device": device,
    }
    try:
        _save_state_to_disk(LED_STATE)
    except Exception:
        # non-fatal: don't break hardware control if disk save fails
        pass


def set_bulb_off(x, y):
    """Turn off bulb at position (x, y).
    x: column index (0-based)
    y: row index (0-based)
    """
    # bounds check
    if y < 0 or y >= len(matrix) or x < 0 or x >= len(matrix[0]):
        raise IndexError("x,y out of range")
    
    device = matrix[y][x]
    
    if DEBUG_PRINTS is True:
        print(f"DEBUG_PRINTS: set_bulb_off({x}, {y})")

    if MQTT_ENABLED is True:
        payload = {"state": "OFF"}
        topic = MQTT_PYTHON_ZIGBEE2MQTT_TOPIC.format(DeviceName=device)
        mqtt.send(topic, payload)

    if SONOFF_ENABLED is True:
        Sonoff_DIY_mode.power(device, False, SONOFF_MS)

    # persist state for future reference; keep last known color_temp/brightness if present
    prev = LED_STATE.get((x, y), {})
    LED_STATE[(x, y)] = {
        "state": "OFF",
        "x": x,
        "y": y,
        "color_temp": prev.get("color_temp"),
        "brightness": prev.get("brightness", 0),
        "device": device,
    }
    try:
        _save_state_to_disk(LED_STATE)
    except Exception:
        pass


def set_all_on_ct(color_temp, brightness, delay: int = 10):
    """Set all bulbs to given temperature and brightness.
    """
    width, height = XY
    for y in range(height):
        for x in range(width):
            set_bulb_on_ct(x, y, color_temp, brightness)
            sleep(delay / (height * width))  # avoid flooding the broker


def set_all_off(delay: int = 10):
    """Turn off all bulbs. 10s incrementing delay to avoid flooding the broker."""
    width, height = XY
    for y in range(height):
        for x in range(width):
            set_bulb_off(x, y)
            sleep(delay / (height * width))  # avoid flooding the broker


def get_state():
    """Return the internal LED state mapping. Keys are (x, y) tuples."""
    # try to load latest from disk so separate processes see updates
    persisted = _load_state_from_disk()
    if persisted:
        # merge persisted into in-memory to keep device names
        for k, v in persisted.items():
            LED_STATE[k] = v
    return LED_STATE


def get_bulb_state(x, y):
    """Return the stored state for a single bulb (x,y)."""
    return LED_STATE.get((x, y))


def map_range(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


## AI made
# Simple in-memory store for LED states keyed by (x, y)
# Each entry will be a dict: {"state": "ON"/"OFF", "x": x, "y": y, "color_temp": int|None, "brightness": int}
LED_STATE = {}

# Path to persist state so multiple processes can share it.
# File is stored in project root next to src/ as "led_state.json".
_STATE_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "led_state.json"))


def _serialize_state(state_dict):
    # convert {(x,y): {...}} -> list of entries for JSON
    out = []
    for (x, y), val in state_dict.items():
        entry = dict(val)
        # ensure x,y are present as ints
        entry["x"] = int(x)
        entry["y"] = int(y)
        out.append(entry)
    return out


def _deserialize_state(entries):
    d = {}
    for e in entries:
        x = int(e.get("x"))
        y = int(e.get("y"))
        d[(x, y)] = {
            "state": e.get("state", "OFF"),
            "x": x,
            "y": y,
            "color_temp": e.get("color_temp"),
            "brightness": e.get("brightness", 0),
            "device": e.get("device"),
        }
    return d


def _save_state_to_disk(state_dict):
    # write atomically to _STATE_FILE
    dirpath = os.path.dirname(_STATE_FILE)
    os.makedirs(dirpath, exist_ok=True)
    data = _serialize_state(state_dict)
    tmp_fd, tmp_path = tempfile.mkstemp(dir=dirpath, prefix=".led_state_tmp_")
    try:
        with os.fdopen(tmp_fd, "w") as f:
            json.dump(data, f)
            f.flush()
            os.fsync(f.fileno())
        # replace the file atomically
        os.replace(tmp_path, _STATE_FILE)
    finally:
        # ensure temp file removed if something went wrong
        if os.path.exists(tmp_path):
            try:
                os.remove(tmp_path)
            except Exception:
                pass


def _load_state_from_disk():
    if not os.path.exists(_STATE_FILE):
        return None
    try:
        with open(_STATE_FILE, "r") as f:
            # place a shared lock while reading
            try:
                fcntl.flock(f.fileno(), fcntl.LOCK_SH)
            except Exception:
                pass
            try:
                data = json.load(f)
            finally:
                try:
                    fcntl.flock(f.fileno(), fcntl.LOCK_UN)
                except Exception:
                    pass
        return _deserialize_state(data)
    except Exception:
        return None