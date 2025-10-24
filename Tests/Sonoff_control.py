'''
AI prompt:

please create a simple python script to control sonoff B05-BL-A60.
I would like to control state, brightness, Color Temperature and Color

here are the commands
avahi-browse -a -r
+ enp8s0 IPv4 eWeLink_10023d8e7d                            _ewelink._tcp        local
= enp8s0 IPv4 eWeLink_10023d8e7d                            _ewelink._tcp        local
   hostname = [eWeLink_10023d8e7d.local]
   address = [192.168.1.221]
   port = [8081]
   txt = ["data1={\"switch\":\"on\",\"ltype\":\"white\",\"white\":{\"br\":100,\"ct\":0},\"slowlyLit\":100,\"slowlyDimmed\":100,\"fwVersion\":\"1.6.0\"}" "seq=1" "apivers=1" "type=diy_light" "id=10023d8e7d" "txtvers=1"]

tomas@fedora:~$ curl -X POST http://192.168.1.221:8081/zeroconf/switch   -H "Content-Type: application/json"   -d '{"data": {"switch": "off"}}'
{"seq":2,"error":0}tomas@fedora:~$

'''


import requests # pip install requests
import json
from time import sleep

DELAY = 1
DEVICE_IP = "192.168.22.221"   # change if your DHCP changes it
BASE_URL = f"http://{DEVICE_IP}:8081/zeroconf"

def send(endpoint, data):
    try:
        r = requests.post(f"{BASE_URL}/{endpoint}", json={"data": data}, timeout=3)
        r.raise_for_status()  # raise if HTTP error
        print(r.text)
        return r.json()
    except requests.RequestException as e:
        print(f"[ERROR] Request failed: {e}")
        return {}  # empty dict so .get() calls won't fail
    except ValueError as e:
        print(f"[ERROR] Invalid JSON response: {e}")
        return {}

def power(on: bool, ms: int):
    send("switch", {"switch": "on" if on else "off", "slowlyLit": ms, "slowlyDimmed": ms})

def color_temp(brightness: int, ct: int, ms: int):
    # 0 = cold white, 255 = warm white (yes, reversed vs Kelvin)
    send("dimmable", {"ltype": "white", "white": {"br": brightness, "ct": ct, "slowlyLit": ms, "slowlyDimmed": ms}})


def rgb(brightness: int, r: int, g: int, b: int, ms: int):
    send("dimmable", {"ltype": "color", "color": {"br": brightness, "r": r, "g": g, "b": b, "slowlyLit": ms, "slowlyDimmed": ms}})


def get_state():
    raw = send("info", {})
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

'''
Bounds:
Brightness: 1-100
Color temperature: 0-100
RGB: 0-255?
'''

if __name__ == "__main__":
    color_temp(1, 100, 100)
    get_state()
