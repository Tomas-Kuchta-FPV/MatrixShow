from time import sleep
from .init import init
# from .led_hal import set_all_off, set_bulb_on_ct, set_bulb_off
from . import led_hal

## Import light effects
from . import LightEffects

SLEEP_INTERVAL = 15  # seconds between effects
EFFECTS_INTERVAL = 8 # seconds between effects

BRIGHTNESS = 100  # Brightness level (1-100)

def main():
    init() # Initialize the application

    while True:
        #LightEffects.love_effect(100, BRIGHTNESS, EFFECTS_INTERVAL)
        #sleep(SLEEP_INTERVAL)
        LightEffects.checkered_effect(100, BRIGHTNESS, EFFECTS_INTERVAL/4)
        sleep(SLEEP_INTERVAL)
        LightEffects.random_effect(False, 0.01, 100)
        sleep(SLEEP_INTERVAL/2)
        led_hal.set_all_off(1)
        LightEffects.zigzag_effect(0, BRIGHTNESS, EFFECTS_INTERVAL/2)
        sleep(SLEEP_INTERVAL/4)
        LightEffects.zigzag_effect(100, BRIGHTNESS, EFFECTS_INTERVAL/4)
        sleep(SLEEP_INTERVAL)
        LightEffects.blink_all_effect(100, BRIGHTNESS, 1, 1)
        LightEffects.blink_all_effect(0, BRIGHTNESS, 1, 1)
        sleep(SLEEP_INTERVAL/4)
        LightEffects.bubacci_effect(30, BRIGHTNESS, EFFECTS_INTERVAL/4)
        sleep(SLEEP_INTERVAL)
        LightEffects.candy_cane_effect(0, BRIGHTNESS, EFFECTS_INTERVAL/2)
        sleep(SLEEP_INTERVAL/2)
        LightEffects.checkered_effect(100, BRIGHTNESS, EFFECTS_INTERVAL/4)
        #LightEffects.love_effect(BRIGHTNESS, 0, EFFECTS_INTERVAL/8)
        sleep(SLEEP_INTERVAL)
        LightEffects.random_effect(False, 0.01, 300)
        #LightEffects.smajlik_effect(100, BRIGHTNESS, EFFECTS_INTERVAL/4)
        sleep(SLEEP_INTERVAL)




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
    LightEffects.candy_cane_effect(100, 5, 2)
    sleep(5)
    LightEffects.blink_all_effect(100, 3, 10, 0.1)


# Call main function
if __name__ == "__main__":
    main()