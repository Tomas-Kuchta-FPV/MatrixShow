from time import sleep
from .init import init
# from .led_hal import set_all_off, set_bulb_on_ct, set_bulb_off

## Import light effects
from . import LightEffects

def main():
    init() # Initialize the application
    everything() # Run all effects


def everything():
    print("EFFECT: Evhery Effect is going to run ;)")
    LightEffects.love_effect()
    LightEffects.blink_all_effect(100, 3, 1, 10)
    LightEffects.random_effect(False, 0.1, 100)
    LightEffects.checkered_effect(100, 5, 0.2)
    LightEffects.zigzag_effect(100, 5, 2)
    LightEffects.candy_cane_effect(100, 5, 2)


# Call main function
if __name__ == "__main__":
    main()