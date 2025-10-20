from time import sleep
from .init import init
# from .led_hal import set_all_off, set_bulb_on_ct, set_bulb_off

## Import light effects
from .LightEffects.blink_all import blink_all
from .LightEffects.random import random_effect
from .LightEffects.checkered import checkered

def main():
    init() # Initialize the application
    everything() # Run all effects


def everything():
    print("EFFECT: Evhery Effect is going to run ;)")
    blink_all(100, 3, 1, 10)
    random_effect(0.2, 200)
    sleep(1)
    checkered(100, 5, 0.5)


# Call main function
if __name__ == "__main__":
    main()