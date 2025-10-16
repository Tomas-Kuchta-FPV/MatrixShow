from .. import led_hal
from time import sleep


def checkered(color_temp: int, brightness: int, delay: float = 0.1):
    """Turn on bulbs in a checkered pattern.
    Even row, even col and odd row, odd col are ON; others OFF.
    """

    # led_hal.XY is a (width, height) tuple; unpack it directly
    width, height = led_hal.XY

    for y in range(height):
        for x in range(width):
            sleep(delay)
            if (x % 2) == (y % 2):
                led_hal.set_bulb_on_ct(x, y, color_temp, brightness)
            else:
                led_hal.set_bulb_off(x, y)