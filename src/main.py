from time import sleep
from .init import init
from .led_hal import set_all_off

## Import light effects
from .LightEffects.blink_all import blink_all
from .LightEffects.random import random_effect

def main():
    init() # Initialize the application


def everything():
    print("Everything is going to run!")
    blink_all(500, 3, 1, 10)
    for i in range(5):
        random_effect(2)
    set_all_off(10)  # Ensure all bulbs are off at the end


# Call main function
if __name__ == "__main__":
    main()