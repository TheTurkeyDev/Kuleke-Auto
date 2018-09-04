import tkinter as tk
import obd
import widgets.Gauge as gauge


class SystemInfoMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        connection = obd.OBD()

        self.test_gauge = gauge.Gauge(self, 0, 100, 10 , 5)

        for item in connection.supported_commands:
            print(item)
