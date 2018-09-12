import tkinter as tk
import obd
import widgets.Gauge as gauge
import serial


class SystemInfoMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.connection = None
        self.controller = controller
        self.connect_odb()

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
            self.add_obd_widgets()
        else:
            print("Failed to find OBD2 device! Retrying in 10 seconds")
            self.controller.after(10000, self.connect_odb)

    def add_obd_widgets(self):
        self.test_gauge = gauge.Gauge(self, 0, 100, 10, 1)
