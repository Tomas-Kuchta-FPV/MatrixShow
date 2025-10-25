from datetime import datetime, time as dtime
from . import config


def parse_hm(hm_str):
    """Parse "HH:MM" into datetime.time or return None on error."""
    try:
        parts = hm_str.split(":")
        return dtime(int(parts[0]) % 24, int(parts[1]) % 60)
    except Exception:
        return None


def is_now_between(on_t, off_t, now=None):
    """Return True if current local time is within [on_t, off_t).
    Handles overnight ranges (e.g., on=22:00, off=06:00).
    """
    if now is None:
        now = datetime.now().time()
    if on_t < off_t:
        return on_t <= now < off_t
    else:
        # overnight
        return now >= on_t or now < off_t


def is_schedule_off():
    """Return True when scheduling is enabled and current time is outside the ON window.

    This encapsulates the check:
      config.SCHEDULE_ENABLED and on_time and off_time and not is_now_between(on_time, off_time)

    It reads times from `config` and returns a boolean; safe to call repeatedly.
    """
    if not getattr(config, "SCHEDULE_ENABLED", False):
        return False
    on_t = parse_hm(getattr(config, "ON_TIME", ""))
    off_t = parse_hm(getattr(config, "OFF_TIME", ""))
    if not on_t or not off_t:
        return False
    return not is_now_between(on_t, off_t)
