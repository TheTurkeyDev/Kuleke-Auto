import tkinter as tk


class SystemInfoMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        b = tk.Button(self, justify=tk.LEFT)
        self.photo = tk.PhotoImage(file="res/icons/nav_icon_96.png")
        b.config(image=self.photo, width="96", height="96")
        b.pack(side=tk.LEFT)
