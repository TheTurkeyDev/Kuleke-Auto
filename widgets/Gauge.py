import tkinter as tk
import math


class Gauge:

    def __init__(self, frame, low, high, tick, subtick):
        self.width = 250
        self.height = 250
        self.half_width = self.width /2
        self.half_hegiht = self.height /2

        self.canvas = tk.Canvas(frame, bg="#282a36", height=self.height, width=self.width, borderwidth=0)

        self.canvas.create_oval(0, 0, self.width, self.height, fill="#282a36", width=2, outline='red')

        self.canvas.create_line(self.width/2, self.height/2, 200, 25, fill='red', arrow=tk.LAST, arrowshape=(130, 90, 10))

        arc_low = 140
        arc_high = 410
        val = low
        for theta in range(arc_low, arc_high, int((arc_high-arc_low)/((high-low + 1)/subtick))):
            theta_rad = math.radians(theta)
            x = math.cos(theta_rad)
            y = math.sin(theta_rad)

            if val % tick == 0:
                line_length = 20
            else:
                line_length = 10

            tx = x * (self.half_width - (line_length + 10)) + self.half_width
            x1 = x * (self.half_width - line_length) + self.half_width
            x2 = x * self.half_width + self.half_width
            ty = y * (self.half_hegiht - (line_length + 10)) + self.half_hegiht
            y1 = y * (self.half_hegiht - line_length) + self.half_hegiht
            y2 = y * self.half_hegiht + self.half_hegiht

            self.canvas.create_line(x1, y1, x2, y2)

            if val % tick == 0:
                self.canvas.create_text(tx, ty, text=val)

            val += subtick

        self.canvas.pack()
