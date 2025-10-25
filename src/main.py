from time import sleep
from .init import init
from .schedule import is_schedule_off

## Import light effects
from . import LightEffects
from . import led_hal

# Show Configuration parameters

SLEEP_INTERVAL = 15  # seconds between effects
EFFECTS_INTERVAL = 8 # seconds between effects

COLOR_TEMP = 80  # Color temperature (0-100)
BRIGHTNESS = 100  # Brightness level (1-100)

# Light show function definitions

def light_show():
    """Run a sequence of light effects."""
    LightEffects.random_effect(COLOR_TEMP, False, 0.01, 100)
    led_hal.set_all_off(1)
    LightEffects.zigzag_effect(0, BRIGHTNESS, EFFECTS_INTERVAL/2)
    sleep(SLEEP_INTERVAL/4)
    LightEffects.zigzag_effect(100, BRIGHTNESS, EFFECTS_INTERVAL/4)
    sleep(SLEEP_INTERVAL)
    LightEffects.blink_all_effect(0, BRIGHTNESS, 2, 1)
    sleep(SLEEP_INTERVAL/4)
    LightEffects.bubacci_effect(COLOR_TEMP, BRIGHTNESS, EFFECTS_INTERVAL/4)
    sleep(SLEEP_INTERVAL)
    led_hal.set_all_off(1)
    LightEffects.candy_cane_effect(COLOR_TEMP, BRIGHTNESS, EFFECTS_INTERVAL/2)
    sleep(SLEEP_INTERVAL/2)
    LightEffects.checkered_effect(0, BRIGHTNESS, EFFECTS_INTERVAL/4)
    LightEffects.snake_ai_effect(COLOR_TEMP, BRIGHTNESS, 3, EFFECTS_INTERVAL)
    sleep(SLEEP_INTERVAL)
    LightEffects.fil_step_effect(COLOR_TEMP,BRIGHTNESS,0.1,3)
    sleep(SLEEP_INTERVAL)


# A python function to run all effects in sequence
def everything():
    print("EFFECT: Evhery Effect is going to run ;)")
    DELAY = 5
    EFFECT_DELAY = 8
    BRIGHTNESS = 10
    COLOR_TEMP = 100

    # love_effect(color_temp, brightness, duration)
    LightEffects.love_effect(COLOR_TEMP, BRIGHTNESS, EFFECT_DELAY)
    sleep(DELAY)
    # blink_all_effect(color_temp, brightness, times, interval)
    LightEffects.blink_all_effect(COLOR_TEMP, BRIGHTNESS, 3, 1)
    sleep(DELAY)
    # random_effect(reverse, interval, color_temp)
    LightEffects.random_effect(True, 0.1, COLOR_TEMP)
    sleep(DELAY)
    # checkered_effect(color_temp, brightness, speed)
    LightEffects.checkered_effect(COLOR_TEMP, BRIGHTNESS, 0.2)
    sleep(DELAY)
    led_hal.set_all_off(DELAY)
    # zigzag_effect(color_temp, brightness, speed)
    LightEffects.zigzag_effect(COLOR_TEMP, BRIGHTNESS, EFFECT_DELAY)
    sleep(DELAY)
    led_hal.set_all_off(DELAY)
    # candy_cane_effect(color_temp, brightness, speed)
    LightEffects.candy_cane_effect(COLOR_TEMP, BRIGHTNESS, EFFECT_DELAY)
    sleep(DELAY)
    # blink_all_effect with different params (times, interval)
    LightEffects.blink_all_effect(COLOR_TEMP, BRIGHTNESS, 3, 0.1)
    sleep(DELAY)
    # bubacci_effect(speed, brightness, repeats)
    LightEffects.bubacci_effect(30, BRIGHTNESS, EFFECT_DELAY)
    sleep(DELAY)
    # smajlik_effect(color_temp, brightness, speed)
    LightEffects.smajlik_effect(COLOR_TEMP, BRIGHTNESS, 2)
    sleep(DELAY)
    LightEffects.snake_ai_effect(COLOR_TEMP,BRIGHTNESS,3,EFFECT_DELAY)



# ----------------------------------
# Main application loop with helpers

def main(): # Entry point
    init() # Initialize the application

    while True:
        # If scheduling indicates we should be OFF, keep LEDs off and re-check shortly.
        if is_schedule_off():
            print("Scheduling: OFF time - turning off LEDs")
            led_hal.set_all_off(1)
            sleep(30)
            continue
        

        print("EFFECT: Starting light show sequence")
        light_show()


# Call main function
if __name__ == "__main__":
    main()