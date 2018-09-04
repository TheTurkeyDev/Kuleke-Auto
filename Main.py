import tkinter as tk
import SystemInfoMenu as SIM
import SettingsMenu as SM


class Main(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.grid_rowconfigure(0, weight=1)  # this needed to be added
        self.grid_columnconfigure(0, weight=1)  # this needed to be added

        self.frames = {}
        menuContainer = tk.Frame(master=self, bg='#282a36')
        menuContainer.grid(column=0, row=0, sticky="nsew")

        navBarFrame = tk.Frame(master=self)
        navBarFrame.grid(column=0, row=1, sticky="nsew")
        navBarFrame.config(bg='#282a36')
        navBarFrame.grid_columnconfigure(0, weight=1)
        navBarFrame.grid_columnconfigure(1, weight=1)
        navBarFrame.grid_columnconfigure(2, weight=1)
        navBarFrame.grid_columnconfigure(3, weight=1)

        b = tk.Button(navBarFrame, justify=tk.LEFT, borderwidth=0, command=lambda: self.button_callback(0))
        self.navIcon = tk.PhotoImage(file="res/icons/nav_icon_96.png")
        b.config(image=self.navIcon, width="96", height="96", bg='#282a36', activebackground='#282a36')
        b.grid(row=1, column=0)

        b = tk.Button(navBarFrame, justify=tk.LEFT, borderwidth=0, command=lambda: self.button_callback(1))
        self.infoIcon = tk.PhotoImage(file="res/icons/info_icon_96.png")
        b.config(image=self.infoIcon, width="96", height="96", bg='#282a36', activebackground='#282a36')
        b.grid(row=1, column=1)

        b = tk.Button(navBarFrame, justify=tk.LEFT, borderwidth=0, command=lambda: self.button_callback(2))
        self.audioIcon = tk.PhotoImage(file="res/icons/audio_icon_96.png")
        b.config(image=self.audioIcon, width="96", height="96", bg='#282a36', activebackground='#282a36')
        b.grid(row=1, column=2)

        b = tk.Button(navBarFrame, justify=tk.LEFT, borderwidth=0, command=lambda: self.button_callback(3))
        self.settingsIcon = tk.PhotoImage(file="res/icons/settings_icon_96.png")
        b.config(image=self.settingsIcon, width="96", height="96", bg='#282a36', activebackground='#282a36')
        b.grid(row=1, column=3)

        self.frames = {}
        for F in (SIM.SystemInfoMenu, SM.SettingsMenu):
            page_name = F.__name__
            frame = F(menuContainer, self)
            frame.config(background='#282a36')
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("SystemInfoMenu")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def button_callback(self, buttonID):
        if buttonID == 1:
            self.show_frame("SystemInfoMenu")
        elif buttonID == 3:
            self.show_frame("SettingsMenu")


if __name__ == "__main__":
    app = Main()
    app.attributes('-fullscreen', True)
    app.mainloop()
