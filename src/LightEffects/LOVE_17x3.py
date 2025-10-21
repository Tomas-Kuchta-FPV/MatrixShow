from time import sleep
from .. import led_hal

def love_effect(brightness = 100, color_temp = 100):
    """
    LOVE effect on the LED matrix.
    """
    print("EFFECT: LOVE_17x3")
    pixel_map = [
        [0,1,0,0,0,1,1,1,0,1,0,1,0,1,1,1,0],
        [0,1,0,0,0,1,0,1,0,1,0,1,0,1,1,0,0],
        [0,1,1,1,0,1,1,1,0,0,1,0,0,1,1,1,0]
    ]

    render_matrix(pixel_map, brightness, color_temp)
    

def render_matrix(pixel_map, brightness, color_temp):
    """Renders a given pixel map on the LED matrix.
    pixel_map: 2D list of 0s and 1s representing off and on states.
    brightness: Brightness level (1-100).
    """
    for y in range(len(pixel_map)):
        for x in range(len(pixel_map[0])):
            sleep(0.1)
            if pixel_map[y][x] == 1:
                led_hal.set_bulb_on_ct(x, y, color_temp, brightness)
            else:
                led_hal.set_bulb_off(x, y)