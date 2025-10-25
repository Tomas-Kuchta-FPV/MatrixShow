import requests # pip install requests

SONOFF_DEBUG = False

def send(ip, endpoint, data):
    try:
        base_url = f"http://{ip}:8081/zeroconf"
        r = requests.post(f"{base_url}/{endpoint}", json={"data": data}, timeout=3)
        r.raise_for_status()  # raise if HTTP error
        if SONOFF_DEBUG:
            print(f"SONOFF: Set IP: {ip}, Endpoint: {endpoint}, Data: {data}")
            print(r.text)
        return r.json()
    except requests.RequestException as e:
        print(f"[ERROR] Request failed: {e}")
        return {}  # empty dict so .get() calls won't fail
    except ValueError as e:
        print(f"[ERROR] Invalid JSON response: {e}")
        return {}

def power(ip, on: bool, ms: int):
    send(ip, "switch", {"switch": "on" if on else "off", "slowlyLit": ms, "slowlyDimmed": ms})

def color_temp(ip, brightness: int, ct: int, ms: int):
    # 0 = cold white, 255 = warm white (yes, reversed vs Kelvin)
    send(ip, "dimmable", {"ltype": "white", "switch": "on", "white": {"br": brightness, "ct": ct, "slowlyLit": ms, "slowlyDimmed": ms}})


def rgb(ip, brightness: int, r: int, g: int, b: int, ms: int):
    send(ip, "dimmable", {"ltype": "color", "color": {"br": brightness, "r": r, "g": g, "b": b, "slowlyLit": ms, "slowlyDimmed": ms}})


def get_state(ip):
    raw = send(ip, "info", {})
    params = raw.get("data", {})

    mode = params.get("ltype", "unknown")
    white = params.get("white", {})
    color = params.get("color", {})

    return {
        "power": params.get("switch"),
        "mode": mode,
        "brightness": white.get("br") if mode == "white" else color.get("br"),
        "color_temp": white.get("ct") if mode == "white" else None,
        "rgb": (
            color.get("r"),
            color.get("g"),
            color.get("b"),
        ) if mode == "color" else None,
        "transition": {
            "slowlyLit": params.get("slowlyLit"),
            "slowlyDimmed": params.get("slowlyDimmed")
        },
        "fwVersion": params.get("fwVersion"),
        "rssi": params.get("rssi"),
        "bssid": params.get("bssid"),
        "deviceid": params.get("deviceid")
    }