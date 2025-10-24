from time import sleep
from .. import led_hal

def render_matrix(pixel_map, brightness, color_temp, delay: float):
    """Renders a given pixel map on the LED matrix.
    pixel_map: 2D list of 0s and 1s representing off and on states.
    brightness: Brightness level (1-100).
    """
    for y in range(len(pixel_map)):
        for x in range(len(pixel_map[0])):
            # Distribute total delay across all pixels; parentheses ensure correct precedence
            sleep(delay / (len(pixel_map) * len(pixel_map[0])))
            if pixel_map[y][x] == 1:
                led_hal.set_bulb_on_ct(x, y, color_temp, brightness)
            else:
                led_hal.set_bulb_off(x, y)