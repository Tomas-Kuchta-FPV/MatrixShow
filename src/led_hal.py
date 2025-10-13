from .config import matrix, MQTT_PYTHON_ZIGBEE2MQTT_TOPIC
from .mqtt import mqtt_send
from time import sleep

def init_leds():
    global XY
    width = len(matrix[0])
    height = len(matrix)
    XY = (width, height)  # X = columns, Y = rows
    print(f"LEDs initialized with dimensions: {XY}")
    return


def set_bulb_on_ct(x, y, color_temp, brightness):
    """Set bulb at position (x, y) to given temperature and brightness.  
    state: True for ON, False for OFF  
    x: column index (0-based)  
    y: row index (0-based)  
    color_temp: color temperature in Kelvin (153-500)  
    brightness: brightness level (0-254)  
    """
    
    # bounds check
    if brightness < 0 or brightness > 254:
        raise ValueError("brightness must be between 0 and 254")
    if color_temp < 153 or color_temp > 500:
        raise ValueError("color_temp must be between 153 and 500")
    if y < 0 or y >= len(matrix) or x < 0 or x >= len(matrix[0]):
        raise IndexError("x,y out of range")
    
    payload = {"color_temp": color_temp, "brightness": brightness, "state": "ON"}
    
    topic = MQTT_PYTHON_ZIGBEE2MQTT_TOPIC.format(DeviceName=matrix[y][x])
    mqtt_send(topic, payload)

def set_bulb_off(x, y):
    """Turn off bulb at position (x, y). 
    x: column index (0-based)  
    y: row index (0-based)  
    """
    # bounds check
    if y < 0 or y >= len(matrix) or x < 0 or x >= len(matrix[0]):
        raise IndexError("x,y out of range")
    
    payload = {"state": "OFF"}
    topic = MQTT_PYTHON_ZIGBEE2MQTT_TOPIC.format(DeviceName=matrix[y][x])
    mqtt_send(topic, payload)

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