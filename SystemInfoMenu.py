import tkinter as tk
import obd


class SystemInfoMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        connection = obd.OBD()

        listbox = tk.Listbox(self)
        listbox.config(width="128", height="128")
        listbox.grid(row=0, column=1)

        listbox.insert(tk.END, "Available Commands")

        for item in connection.supported_commands:
            listbox.insert(tk.END, item)
