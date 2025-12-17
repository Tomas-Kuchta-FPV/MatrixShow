from time import sleep
from .. import led_hal


def _get_start_coords():
    if not hasattr(led_hal, "XY"):
        raise RuntimeError("led_hal.XY not initialized; call led_hal.init_leds() before dice_effect()")
    width, height = led_hal.XY
    # center a 3x3 dice in the available matrix
    start_x = max(0, (width - 3) // 2)
    start_y = max(0, (height - 3) // 2)
    return start_x, start_y


_PIPS = {
    1: [(1, 1)],
    2: [(0, 0), (2, 2)],
    3: [(0, 0), (1, 1), (2, 2)],
    4: [(0, 0), (0, 2), (2, 0), (2, 2)],
    5: [(0, 0), (0, 2), (1, 1), (2, 0), (2, 2)],
    6: [(0, 0), (0, 1), (0, 2), (2, 0), (2, 1), (2, 2)],
}


def _draw_face(face: int, color_temp: int, brightness: int):
    sx, sy = _get_start_coords()
    # ensure face valid
    face = max(1, min(6, int(face)))
    pips = set(_PIPS[face])
    for yy in range(3):
        for xx in range(3):
            gx = sx + xx
            gy = sy + yy
            if (xx, yy) in pips:
                led_hal.set_bulb_on_ct(gx, gy, color_temp, brightness)
            else:
                led_hal.set_bulb_off(gx, gy)


def dice_effect(color_temp: int, brightness: int, mode: str = "cycle", cycles: int = 3, interval: float = 0.8, number: int = 1):
    """Display a 3x3 dice.

    Modes:
    - "cycle": animate faces 1..6 for `cycles` iterations
    - "number": display the given `number` (1-6) for `cycles` iterations

    Parameters:
    - `color_temp`, `brightness` -- passed to `led_hal.set_bulb_on_ct`
    - `interval` -- seconds between frames
    - `number` -- used when mode == "number"
    """
    print("EFFECT: dice_effect(mode=%s, cycles=%d)" % (mode, cycles))
    if mode not in ("cycle", "number"):
        raise ValueError("mode must be 'cycle' or 'number'")

    if mode == "cycle":
        for _ in range(max(1, cycles)):
            for face in range(1, 7):
                _draw_face(face, color_temp, brightness)
                sleep(interval)
    else:
        for _ in range(max(1, cycles)):
            _draw_face(number, color_temp, brightness)
            sleep(interval)
