from time import sleep
from .. import led_hal
from .Renderer import render_matrix

def love_effect(brightness = 100, color_temp = 100, delay: float = 1.0):
    """
    LOVE effect on the LED matrix.
    """
    print("EFFECT: LOVE_17x3")
    pixel_map = [
        [0,1,0,0,0,1,1,1,0,1,0,1,0,1,1,1,0],
        [0,1,0,0,0,1,0,1,0,1,0,1,0,1,1,0,0],
        [0,1,1,1,0,1,1,1,0,0,1,0,0,1,1,1,0]
    ]

    render_matrix(pixel_map, brightness, color_temp, delay)