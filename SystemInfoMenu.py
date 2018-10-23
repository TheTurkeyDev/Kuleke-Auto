import tkinter as tk
import obd
from obd.decoders import pid, single_dtc
import widgets.Gauge as Gauge
import serial


class SystemInfoMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.widgets_canvas = tk.Frame(master=self, bg='#282a36')
        self.widgets_canvas.grid(column=0, row=1, sticky="nsew")

        self.widgets = []
        self.connection = None
        self.controller = controller
        self.connect_odb()

        new_widget_button = tk.Button(self, text="+", justify=tk.RIGHT, borderwidth=0, command=self.new_widget)
        new_widget_button.grid(row=0, column=0, padx=10, pady=10)
        self.add_obd_widgets()

    def connect_odb(self):
        #TODO: Add some sort of loading signal
        ports = obd.scan_serial()
        for port in ports:

            passes = True
            try:
                self.connection = obd.OBD(port)
            except serial.serialutil.SerialException:
                passes = False

            if passes:
                break

        if self.connection is not None and self.connection.is_connected():
            self.update_obd_widgets()
        else:
            print("Failed to find OBD2 device! Retrying in 10 seconds")
            self.controller.after(10000, self.connect_odb)

    def add_obd_widgets(self):
        test = Gauge.Gauge(self.widgets_canvas, 0, 100, 10, 1)
        self.widgets.append(test)

    def update_obd_widgets(self):
        print("here")

    def new_widget(self):
        widget_win = tk.Toplevel()
        widget_win.geometry('300x300')
        widget_win.wm_title("New Widget")

        widget_win.grid_columnconfigure(0, weight=1)
        widget_win.grid_rowconfigure(1, weight=1)

        frame = tk.Frame(widget_win)
        scrollbar = tk.Scrollbar(frame)
        listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set)
        scrollbar.config(command=listbox.yview)
        frame.grid(row=1, column=0, sticky='ew')
        scrollbar.pack(side=tk.RIGHT, fill="both")
        listbox.pack(fill="both")

        label = tk.Label(widget_win, text="Add new Widget")
        label.grid(row=0, column=0)

        add = tk.Button(widget_win, text="Add")
        add.grid(row=2, column=0)

        for command in obd.commands.modes[1]:
            if command.decode != pid and command.decode != single_dtc:
                text = command.name
                if self.connection is not None and self.connection.is_connected() and not obd.commands.has_command(command):
                    text += " (Not Supported)"
                listbox.insert(tk.END, text)
