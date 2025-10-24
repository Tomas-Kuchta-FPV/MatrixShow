from time import sleep
from .. import led_hal

def candy_cane_effect(color_temp, brightness,delay):

    print("EFFECT: candy_cane_effect()")

    width, height = led_hal.XY
    
    y = height - 1
    for x in range(width):
        led_hal.set_bulb_on_ct(x, y , color_temp, brightness)
        sleep(delay/width)
        y -= 1
        if y < 0:
            y = height -1
