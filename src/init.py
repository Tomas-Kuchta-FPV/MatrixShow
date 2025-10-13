from .mqtt import mqtt_init
from .led_hal import init_leds

def init():
    mqtt_init() ## init mqtt
    init_leds() ## init leds
    print("Initialization complete")