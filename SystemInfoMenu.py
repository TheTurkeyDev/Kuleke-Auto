import tkinter as tk
import obd
import widgets.Gauge as gauge


class SystemInfoMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.connect_odb()

    def connect_odb(self):
        #TODO: Add some sort of loading signal

        self.connection = obd.OBD()
        if self.connection.is_connected():
            self.add_obd_widgets()
        else:
            self.controller.after(10000, self.connect_odb)

    def add_obd_widgets(self):
        self.test_gauge = gauge.Gauge(self, 0, 100, 10, 1)

        for item in self.connection.supported_commands:
            print(item)
