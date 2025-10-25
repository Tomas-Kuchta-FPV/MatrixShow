from time import sleep
from .. import led_hal
from .. import config

## AI made

def fil_step_effect(color_temp: int, brightness: int, delay: float = 1.1, step: int = 3):
    print("EFFECT: fil_step_effect()")

    width, height = led_hal.XY

    # Validate step
    if step is None or step < 1:
        step = 3

    # Iterate columns in groups of `step` columns (0..width-1)
    for x in range(0, width, step):
        # Turn on group: columns x .. x+step-1 (bounded by width)
        for col in range(x, min(x + step, width)):
            for y in range(height):
                led_hal.set_bulb_on_ct(col, y, color_temp, brightness)
                #sleep(delay)


        # Turn off the same group
        for col in range(x, min(x + step, width)):
            for y in range(height):
                led_hal.set_bulb_off(col, y)
                #sleep(delay)