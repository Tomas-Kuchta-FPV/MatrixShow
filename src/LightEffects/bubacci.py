from .. import led_hal
from .Renderer import render_matrix

def bubacci_effect(color_temp, brightness, delay):
    print("EFFECT: bubacci_effect()")
    pixel_map = [
        [0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0],
        [1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1],
        [0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0]
    ]

    render_matrix(pixel_map, brightness, color_temp, delay)