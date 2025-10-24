"""
AI magic code
A simple Tkinter GUI to control an LED matrix defined in config.py.
Each LED is represented as a rectangle that can be toggled on/off by clicking.

Install deps by running:
sudo dnf install python3-tkinter
Run it with:
python -m Tools.GUI
"""

import threading
import tkinter as tk
from functools import partial

from src.config import matrix
from src.led_hal import init_leds, set_bulb_on_ct, set_bulb_off, set_all_on_ct, set_all_off, get_state

# Default visual settings
LED_SIZE = 48
PADDING = 40
DEFAULT_COLOR_TEMP = 100  # within allowed 153-500
DEFAULT_BRIGHTNESS = 1  # within allowed 0-254
INTERPOLATION_DELAY = 1  # seconds for bulk on/off


class LEDMatrixGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("LED Matrix Display")
        self.Bulk_Operation = False

        if not matrix or not matrix[0]:
            raise RuntimeError("matrix in config.py is empty or malformed")

        self.rows = len(matrix)
        self.cols = len(matrix[0])

        canvas_width = self.cols * (LED_SIZE + PADDING) + PADDING
        canvas_height = self.rows * (LED_SIZE + PADDING) + PADDING

        self.canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="black")
        self.canvas.pack(padx=6, pady=6)

        # Maps (row,col) -> {'rect': id, 'state': bool}
        self.leds = {}

        for r in range(self.rows):
            for c in range(self.cols):
                x1 = PADDING + c * (LED_SIZE + PADDING)
                y1 = PADDING + r * (LED_SIZE + PADDING)
                x2 = x1 + LED_SIZE
                y2 = y1 + LED_SIZE

                rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill="gray20", outline="gray40")
                # store state (False = OFF)
                self.leds[(r, c)] = {"rect": rect, "state": False}
                # attach tags so we can look up row/col on click
                self.canvas.tag_bind(rect, "<Button-1>", partial(self._on_click, r, c))

        # Controls
        ctrl_frame = tk.Frame(root)
        ctrl_frame.pack(pady=(6, 12))

        # Store button refs so we can disable/enable during bulk ops
        self.on_all_btn = tk.Button(ctrl_frame, text="All ON", command=self.turn_all_on)
        self.on_all_btn.pack(side=tk.LEFT, padx=4)

        self.off_all_btn = tk.Button(ctrl_frame, text="All OFF", command=self.turn_all_off)
        self.off_all_btn.pack(side=tk.LEFT, padx=4)

        self.refresh_btn = tk.Button(ctrl_frame, text="Refresh (assume OFF)", command=self.refresh_display)
        self.refresh_btn.pack(side=tk.LEFT, padx=4)

        # Lock to prevent concurrent bulk operations (turn_all_on / turn_all_off)
        self.bulk_lock = threading.Lock()

        # Sync initial display with real LED states
        try:
            self.refresh_display()
        except Exception as e:
            # Don't crash the GUI if hardware state isn't available
            print(f"refresh_display failed during init: {e}")

        # Schedule periodic refresh so multiple processes (main and GUI) stay in sync.
        # Runs on the Tk mainloop thread every 1000ms.
        self._schedule_periodic_refresh()

    def _schedule_periodic_refresh(self, interval_ms: int = 100):
        try:
            self.refresh_display()
        finally:
            # re-schedule
            self.root.after(interval_ms, self._schedule_periodic_refresh)

    def _spawn(self, fn, *args, **kwargs):
        """Run fn in a background thread to avoid blocking the GUI."""
        t = threading.Thread(target=fn, args=args, kwargs=kwargs, daemon=True)
        t.start()

    def _on_click(self, row, col, event=None):
        # If a bulk operation is in progress, ignore individual toggles
        if getattr(self, "bulk_lock", None) and self.bulk_lock.locked():
            # Optional: give a visual cue or log
            print(f"Ignoring click at ({row},{col}) during bulk operation")
            return

        entry = self.leds.get((row, col))
        if entry is None:
            return

        new_state = not entry["state"]
        entry["state"] = new_state

        if new_state:
            # Turn on with default CT and brightness
            self._set_rect_color(entry["rect"], True)
            # Call hardware function in background
            self._spawn(set_bulb_on_ct, col, row, DEFAULT_COLOR_TEMP, DEFAULT_BRIGHTNESS)
        else:
            self._set_rect_color(entry["rect"], False)
            self._spawn(set_bulb_off, col, row)

    def _set_rect_color(self, rect_id, on: bool):
        color = "#7CFC00" if on else "gray20"  # lawn green when on
        self.canvas.itemconfig(rect_id, fill=color)

    def _set_warning(self, row, col):
        entry = self.leds.get((row, col))
        if entry:
            self.canvas.itemconfig(entry["rect"], fill="orange")

    def start_bulk_operation(self):
        self.bulk_lock.acquire()
        self.on_all_btn.config(state=tk.DISABLED)
        self.off_all_btn.config(state=tk.DISABLED)
        self.refresh_btn.config(state=tk.DISABLED)

    def end_bulk_operation(self):
        self.on_all_btn.config(state=tk.NORMAL)
        self.off_all_btn.config(state=tk.NORMAL)
        self.refresh_btn.config(state=tk.NORMAL)
        self.bulk_lock.release()

    def turn_all_on(self):
        # Prevent concurrent bulk ops
        if getattr(self, "bulk_lock", None) and self.bulk_lock.locked():
            return
        self.start_bulk_operation()

        def _worker():
            try:
                # perform the potentially slow hardware calls off the GUI thread
                set_all_on_ct(DEFAULT_COLOR_TEMP, DEFAULT_BRIGHTNESS, INTERPOLATION_DELAY)
            except Exception as e:
                print(f"Error during turn_all_on: {e}")
                # ensure buttons are re-enabled even on error
                self.root.after(0, self.end_bulk_operation)
                return

            def _mark_on():
                for entry in self.leds.values():
                    entry["state"] = True
                    self._set_rect_color(entry["rect"], True)
                # re-enable buttons and release lock on the GUI thread
                self.end_bulk_operation()

            self.root.after(0, _mark_on)

        self._spawn(_worker)

    def turn_all_off(self):
        # Prevent concurrent bulk ops
        if getattr(self, "bulk_lock", None) and self.bulk_lock.locked():
            return
        self.start_bulk_operation()

        def _worker():
            try:
                set_all_off(INTERPOLATION_DELAY)
            except Exception as e:
                print(f"Error during turn_all_off: {e}")
                self.root.after(0, self.end_bulk_operation)
                return

            def _mark_off():
                for entry in self.leds.values():
                    entry["state"] = False
                    self._set_rect_color(entry["rect"], False)
                self.end_bulk_operation()

            self.root.after(0, _mark_off)

        self._spawn(_worker)

    def refresh_display(self):
        # Read the stored state from led_hal.get_state() and update the GUI.
        try:
            led_state = get_state() or {}
        except Exception:
            led_state = {}

        for (row, col), entry in self.leds.items():
            # led_state uses (x,y) == (col,row)
            bulb = led_state.get((col, row))
            is_on = False
            if bulb and bulb.get("state") == "ON":
                is_on = True

            entry["state"] = is_on
            self._set_rect_color(entry["rect"], is_on)


def main():
    # Initialize hardware helper (sets XY in led_hal)
    try:
        init_leds()
    except Exception as e:
        print(f"Warning: init_leds failed: {e}")

    root = tk.Tk()
    app = LEDMatrixGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
