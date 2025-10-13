# AI
import tkinter as tk
from .led_hal import XY
# sudo dnf install python3-tkinter

# Matrix size
LED_SIZE = 40  # pixel size of each LED

def gui_init(self, root):
    self.root = root
    self.root.title("LED Matrix Display")

    # Create canvas
    x, y = XY

    self.canvas = tk.Canvas(root, width=x * LED_SIZE, height=y * LED_SIZE, bg="black")
    self.canvas.pack()

    # Store LED rectangles and states
    self.leds = {}
    for r in range(y):
        for c in range(x):
            x1 = c * LED_SIZE
            y1 = r * LED_SIZE
            x2 = x1 + LED_SIZE
            y2 = y1 + LED_SIZE

            rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill="gray20", outline="gray40")
            self.leds[rect] = False  # False = OFF
            self.canvas.tag_bind(rect, "<Button-1>", self.toggle_led)

def toggle_led(self, event):
    rect = self.canvas.find_withtag("current")[0]
    state = not self.leds[rect]
    self.leds[rect] = state

    color = "lime" if state else "gray20"
    self.canvas.itemconfig(rect, fill=color)
