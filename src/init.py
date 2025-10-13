from time import sleep
from .mqtt import mqtt_init
from .led_hal import init_leds, set_all_off

def init():
    mqtt_init() ## init mqtt
    init_leds() ## init leds
    sleep(0.5)
    set_all_off(5) # Ensure all lights are off at start
    sleep(1)
    print("Initialization complete")
    