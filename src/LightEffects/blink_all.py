from time import sleep
from .. import led_hal


def blink_all_effect(color_temp: int, brightness: int, blink_count: int = 2, blink_delay: int = 20) -> None:
    """Blink all bulbs simultaneously blink_count times.
    Ensures all bulbs are turned off on exit.

    Notes:
    - `led_hal.init_leds()` must be called before this function so `led_hal.XY` is available.
    """
    if blink_count <= 0 or blink_delay <= 0:
        return

    if not hasattr(led_hal, "XY"):
        raise RuntimeError("led_hal.XY not initialized; call led_hal.init_leds() before blink_all_effect()")

    width, height = led_hal.XY

    print("EFFECT: blink_all_effect()")

    for _ in range(blink_count):
        led_hal.set_all_on_ct(color_temp, brightness, blink_delay/4)
        sleep(blink_delay/4)
        led_hal.set_all_off(blink_delay/4)
        sleep(blink_delay/4)