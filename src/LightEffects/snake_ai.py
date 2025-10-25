from time import sleep
from collections import deque
from .. import led_hal

## AI made
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

    # compute per-action sleep so `delay` approximates the total runtime
    # total actions = number of head moves (width*height) + cleanup turns (expected trail length)
    if delay is None or delay <= 0:
        per_step_sleep = 0.0
    else:
        if tail is None or tail <= 0:
            expected_trail_len = 0
        else:
            expected_trail_len = min(tail + 1, width * height)
        total_actions = width * height + expected_trail_len
        per_step_sleep = float(delay) / total_actions if total_actions > 0 else 0.0

    # if tail is not positive, behave like original simple snake but use per_step_sleep
    if tail is None or tail <= 0:
        for x in range(width):
            for y in range(height):
                led_hal.set_bulb_on_ct(x, y, color_temp, brightness)
                if per_step_sleep:
                    sleep(per_step_sleep)
                led_hal.set_bulb_off(x, y)
        return

    # maintain recent positions as deque of (x,y)
    # use an unbounded deque and manually pop oldest entries so we can turn off
    # only the exact LED that left the trail instead of clearing the whole matrix
    trail = deque()

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

            # if the trail is now longer than allowed, pop the oldest and turn THAT one off only
            maxlen = (tail + 1) if tail is not None and tail >= 0 else None
            if maxlen is not None and len(trail) > maxlen:
                # oldest coordinate goes to the right end
                removed = trail.pop()
                rx, ry = removed
                # turn off that specific LED if it's still ON
                state = led_hal.get_bulb_state(rx, ry)
                if state and state.get("state") == "ON":
                    led_hal.set_bulb_off(rx, ry)

            if per_step_sleep:
                sleep(per_step_sleep)

    # after finishing the traversal, clear out any remaining trail so no LEDs stay lit
    while trail:
        tx, ty = trail.popleft()
        state = led_hal.get_bulb_state(tx, ty)
        if state and state.get("state") == "ON":
            led_hal.set_bulb_off(tx, ty)
        # small pause so hardware/broker isn't flooded; use per-step sleep so total runtime ~= delay
        if per_step_sleep:
            sleep(per_step_sleep)