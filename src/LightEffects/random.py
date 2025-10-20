import random
import time
from .. import led_hal


def random_effect(change_interval: int = 5, cycles: int = 10):
    # led_hal.XY is a (width, height) tuple
    width, height = led_hal.XY
    print("EFFECT: random_effect()")

    for i in range(cycles):
        r_x = random.randint(0, width - 1)
        r_y = random.randint(0, height - 1)
        r_ct = random.randint(0, 100)  # color temp range
        r_brightness = random.randint(1, 100)  # brightness range

        led_hal.set_bulb_on_ct(r_x, r_y, r_ct, r_brightness)

        r_x = random.randint(0, width - 1)
        r_y = random.randint(0, height - 1)
        led_hal.set_bulb_off(r_x, r_y)  # turn it off

        time.sleep(change_interval)