from time import sleep
from .init import init
# from .led_hal import set_all_off, set_bulb_on_ct, set_bulb_off
from . import led_hal

## Import light effects
from . import LightEffects

def main():
    init() # Initialize the application
    everything() # Run all effects


def everything():
    print("EFFECT: Evhery Effect is going to run ;)")
    LightEffects.love_effect()
    sleep(5)
    LightEffects.blink_all_effect(100, 3, 1, 10)
    sleep(5)
    LightEffects.random_effect(True, 0.1, 100)
    sleep(5)
    LightEffects.checkered_effect(100, 5, 0.2)
    sleep(5)
    led_hal.set_all_off(5)
    LightEffects.zigzag_effect(100, 5, 2)
    sleep(5)
    led_hal.set_all_off(5)
    sleep(5)
    LightEffects.candy_cane_effect(100, 5, 2)
    sleep(5)
    LightEffects.blink_all_effect(100, 3, 10, 0.1)


# Call main function
if __name__ == "__main__":
    main()