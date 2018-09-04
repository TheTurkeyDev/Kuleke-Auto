import tkinter as tk
import math


class Gauge:

    def __init__(self, frame, low, high):
        self.width = 250
        self.height = 250
        self.half_width = self.width /2
        self.half_hegiht = self.height /2

        self.canvas = tk.Canvas(frame, bg="#282a36", height=self.height, width=self.width, borderwidth=0)

        self.canvas.create_oval(0, 0, self.width, self.height, fill="#282a36", width=2, outline='red')

        self.canvas.create_line(self.width/2, self.height/2, 200, 25, fill='red', arrow=tk.LAST, arrowshape=(130, 90, 10))

        arc_low = 140
        arc_high = 420
        for theta in range(arc_low, arc_high, 25):
            theta_rad = math.radians(theta)
            x = math.cos(theta_rad)
            y = math.sin(theta_rad)
            x1 = x * (self.half_width - 20) + self.half_width
            x2 = x * self.half_width + self.half_width
            y1 = y * (self.half_hegiht - 20) + self.half_hegiht
            y2 = y * self.half_hegiht + self.half_hegiht

            self.canvas.create_line(x1, y1, x2, y2)
            val = self.map(theta, arc_low, arc_high, low, high)
            self.canvas.create_text(x1, y1, text=val)

        self.canvas.pack()

    def map(self, current_value, old_low,  old_upper,  new_low, new_upper):
        return (current_value - old_low) / (old_upper - old_low) * (new_upper - new_low) + new_low
