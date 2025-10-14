import threading
import tkinter as tk
from functools import partial

from src.config import matrix
from src.led_hal import init_leds, set_bulb_on_ct, set_bulb_off

# Default visual settings
LED_SIZE = 48
PADDING = 4
DEFAULT_COLOR_TEMP = 300  # within allowed 153-500
DEFAULT_BRIGHTNESS = 200  # within allowed 0-254


class LEDMatrixGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("LED Matrix Display")

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

        on_all_btn = tk.Button(ctrl_frame, text="All ON", command=self.turn_all_on)
        on_all_btn.pack(side=tk.LEFT, padx=4)

        off_all_btn = tk.Button(ctrl_frame, text="All OFF", command=self.turn_all_off)
        off_all_btn.pack(side=tk.LEFT, padx=4)

        refresh_btn = tk.Button(ctrl_frame, text="Refresh (assume OFF)", command=self.refresh_display)
        refresh_btn.pack(side=tk.LEFT, padx=4)

    def _spawn(self, fn, *args, **kwargs):
        """Run fn in a background thread to avoid blocking the GUI."""
        t = threading.Thread(target=fn, args=args, kwargs=kwargs, daemon=True)
        t.start()

    def _on_click(self, row, col, event=None):
        entry = self.leds.get((row, col))
        if entry is None:
            return

        new_state = not entry["state"]
        entry["state"] = new_state

        if new_state:
            # Turn on with default CT and brightness
            self._set_rect_color(entry["rect"], True)
            # Call hardware function in background
            self._spawn(self._safe_set_on, col, row, DEFAULT_COLOR_TEMP, DEFAULT_BRIGHTNESS)
        else:
            self._set_rect_color(entry["rect"], False)
            self._spawn(self._safe_set_off, col, row)

    def _safe_set_on(self, x, y, color_temp, brightness):
        try:
            set_bulb_on_ct(x, y, color_temp, brightness)
        except Exception as e:
            # If hardware call fails, reflect it in the UI by setting the LED to a warning color
            self.root.after(0, self._set_warning, y, x)
            print(f"Error setting bulb on at ({x},{y}): {e}")

    def _safe_set_off(self, x, y):
        try:
            set_bulb_off(x, y)
        except Exception as e:
            self.root.after(0, self._set_warning, y, x)
            print(f"Error setting bulb off at ({x},{y}): {e}")

    def _set_rect_color(self, rect_id, on: bool):
        color = "#7CFC00" if on else "gray20"  # lawn green when on
        self.canvas.itemconfig(rect_id, fill=color)

    def _set_warning(self, row, col):
        entry = self.leds.get((row, col))
        if entry:
            self.canvas.itemconfig(entry["rect"], fill="orange")

    def turn_all_on(self):
        for (r, c), entry in self.leds.items():
            entry["state"] = True
            self._set_rect_color(entry["rect"], True)
            # spawn hardware call
            self._spawn(self._safe_set_on, c, r, DEFAULT_COLOR_TEMP, DEFAULT_BRIGHTNESS)

    def turn_all_off(self):
        for (r, c), entry in self.leds.items():
            entry["state"] = False
            self._set_rect_color(entry["rect"], False)
            # spawn hardware call
            self._spawn(self._safe_set_off, c, r)

    def refresh_display(self):
        # There's no read-back API in led_hal; assume OFF for safety.
        for entry in self.leds.values():
            entry["state"] = False
            self._set_rect_color(entry["rect"], False)


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
