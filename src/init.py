from time import sleep
from .Protocols.mqtt import mqtt_init
from .led_hal import init_leds, set_all_off
from .config import MQTT_ENABLED

def init():
    if MQTT_ENABLED:
        mqtt_init() ## init mqtt
    init_leds() ## init leds
    sleep(0.5)
    print("INIT: Turning all lights off")
    set_all_off(5) # Ensure all lights are off at start
    sleep(1)
    print("INIT: Initialization complete")
    