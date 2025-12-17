# SvU light show
Here are the setting used for the light show.

## Videos & Photos
**TODO**

## Time spent
### HW
*30h*
### SW
*40h*
### Brainstorming & Preparation
*10h*


## LightShow program
``` python
SLEEP_INTERVAL = 15
EFFECTS_INTERVAL = 8

COLOR_TEMP = 80
BRIGHTNESS = 100

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
    led_hal.set_all_off(1)
    LightEffects.snake_ai_effect(COLOR_TEMP, BRIGHTNESS, 8, EFFECTS_INTERVAL)
    sleep(SLEEP_INTERVAL)
    LightEffects.fil_step_effect(COLOR_TEMP,BRIGHTNESS,0.1,3)
    sleep(SLEEP_INTERVAL)
```
