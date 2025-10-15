import random
import time
from .. import led_hal


def random_effect(change_interval: int = 5):
    
    r_x = random.randint(0, led_hal.XY[0] - 1)
    r_y = random.randint(0, led_hal.XY[1] - 1)
    r_ct = random.randint(153, 500)  # color temp range
    r_brightness = random.randint(0, 254)  # brightness range

    led_hal.set_bulb_on_ct(r_x, r_y, r_ct, r_brightness)

    r_x = random.randint(0, led_hal.XY[0] - 1)
    r_y = random.randint(0, led_hal.XY[1] - 1)
    led_hal.set_bulb_off(r_x, r_y)  # turn it off

    time.sleep(change_interval)