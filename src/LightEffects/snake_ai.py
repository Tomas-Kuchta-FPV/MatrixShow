from time import sleep
from collections import deque
from .. import led_hal


def _clamp(v, lo, hi):
    return max(lo, min(hi, v))


def snake_ai_effect(color_temp, brightness, tail: int, delay: float):
    """Snake effect moving from top-left to bottom-right with a fading trail.

    color_temp: int (0-100)
    brightness: int (1-100) brightness of the head
    tail: number of additional LEDs that form the trail (0 -> no trail)
    delay: seconds between head moves
    """
    print("EFFECT: snake_effect()")

    # derive dimensions from led_hal
    if not hasattr(led_hal, "matrix"):
        raise RuntimeError("led_hal.matrix not available; ensure leds are initialized")
    width = len(led_hal.matrix[0])
    height = len(led_hal.matrix)

    # if tail is not positive, behave like original simple snake but with configurable delay
    if tail is None or tail <= 0:
        for x in range(width):
            for y in range(height):
                led_hal.set_bulb_on_ct(x, y, color_temp, brightness)
                sleep(delay)
                led_hal.set_bulb_off(x, y)
        return

    # maintain recent positions as deque of (x,y)
    trail = deque(maxlen=tail + 1)  # include head

    # iterate left-to-right, but alternate vertical direction per column
    for x in range(width):
        # even columns: top->bottom (y = 0..height-1)
        # odd columns: bottom->top (y = height-1..0)
        if x % 2 == 0:
            y_range = range(0, height)
        else:
            y_range = range(height - 1, -1, -1)

        for y in y_range:
            # add new head
            trail.appendleft((x, y))

            # update LEDs in the trail: head gets full brightness, tail fades linearly
            for idx, (tx, ty) in enumerate(trail):
                # idx == 0 is head
                if idx == 0:
                    b = _clamp(int(brightness), 1, 100)
                else:
                    # fade: position further back is dimmer
                    # compute factor from  (tail) -> 0.1..0.9
                    frac = 1.0 - (idx / float(len(trail)))
                    # ensure minimum visibility 1
                    b = _clamp(int(max(1, round(brightness * frac))), 1, 100)

                # if brightness becomes 0 logically, turn off
                if b <= 0:
                    led_hal.set_bulb_off(tx, ty)
                else:
                    led_hal.set_bulb_on_ct(tx, ty, color_temp, b)

            # if the deque filled beyond maxlen the oldest was removed automatically; ensure the removed spot is off
            # because maxlen auto discards, we can compute the next-oldest position to turn off
            if len(trail) == trail.maxlen:
                # the last element in deque is the tail end that should remain lit; the one removed (if any) should be off
                # to safely turn off any LED not in trail, we can compute all coordinates and turn off ones not present
                present = set(trail)
                # quick pass to turn off any LED that was previously on but is no longer part of the trail
                # iterate over the full matrix and turn off bulbs not in present that have state ON
                for yy in range(height):
                    for xx in range(width):
                        if (xx, yy) not in present:
                            # consult stored state to avoid unnecessary MQTT calls
                            state = led_hal.get_bulb_state(xx, yy)
                            if state and state.get("state") == "ON":
                                led_hal.set_bulb_off(xx, yy)

            sleep(delay)