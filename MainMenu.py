import tkinter as tk


class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        b = tk.Button(self, justify=tk.LEFT, borderwidth=0, command=lambda: self.button_callback(0))
        self.navIcon = tk.PhotoImage(file="res/icons/nav_icon_96.png")
        b.config(image=self.navIcon, width="96", height="96", bg='#282a36', activebackground='#282a36')
        b.grid(row=1, column=0)

        b = tk.Button(self, justify=tk.LEFT, borderwidth=0, command=lambda: self.button_callback(1))
        self.infoIcon = tk.PhotoImage(file="res/icons/info_icon_96.png")
        b.config(image=self.infoIcon, width="96", height="96", bg='#282a36', activebackground='#282a36')
        b.grid(row=1, column=1)

        b = tk.Button(self, justify=tk.LEFT, borderwidth=0, command=lambda: self.button_callback(2))
        self.audioIcon = tk.PhotoImage(file="res/icons/audio_icon_96.png")
        b.config(image=self.audioIcon, width="96", height="96", bg='#282a36', activebackground='#282a36')
        b.grid(row=1, column=2)

        b = tk.Button(self, justify=tk.LEFT, borderwidth=0, command=lambda: self.button_callback(3))
        self.settingsIcon = tk.PhotoImage(file="res/icons/settings_icon_96.png")
        b.config(image=self.settingsIcon, width="96", height="96", bg='#282a36', activebackground='#282a36')
        b.grid(row=1, column=3)

    def button_callback(self, buttonID):
        if buttonID == 1:
            self.controller.show_frame("SystemInfoMenu")
        elif buttonID == 3:
            self.controller.show_frame("SettingsMenu")

