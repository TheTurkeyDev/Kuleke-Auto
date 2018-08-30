import tkinter as tk
import MainMenu as MM
import SystemInfoMenu as SIM
import SettingsMenu as SM


class Main(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.grid_rowconfigure(0, weight=1)  # this needed to be added
        self.grid_columnconfigure(0, weight=1)  # as did this

        self.frames = {}
        container = tk.Frame(self)
        container.grid(column=0, row=0, sticky="nsew")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (MM.MainMenu, SIM.SystemInfoMenu, SM.SettingsMenu):
            page_name = F.__name__
            frame = F(container, self)
            frame.config(background='#282a36')
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainMenu")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


if __name__ == "__main__":
    app = Main()
    app.attributes('-fullscreen', True)
    app.mainloop()
