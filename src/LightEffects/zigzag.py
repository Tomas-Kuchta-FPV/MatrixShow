from time import sleep
from .. import led_hal

def zigzag_effect(color_temp, brightness, delay):

    width, height = led_hal.XY
    print("EFFECT: zigzag_effect()")

    # AI Helped with this function
    # If there's only one row, just draw the row for each column
    if height <= 1:
        y = 0
        for x in range(width):
            led_hal.set_bulb_on_ct(x, y, color_temp, brightness)
            sleep(delay)
        return

    # Start at the bottom and move up; when we hit an edge, reverse direction
    y = height - 1
    dy = -1
    for x in range(width):
        led_hal.set_bulb_on_ct(x, y, color_temp, brightness)
        sleep(delay/width)
        y += dy
        # Bounce at the top
        if y < 0:
            y = 1 if height > 1 else 0
            dy = 1
        # Bounce at the bottom
        elif y >= height:
            y = height - 2 if height > 1 else 0
            dy = -1
