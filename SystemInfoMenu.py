import tkinter as tk
import obd
import widgets.Gauge as Gauge
import serial


class SystemInfoMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.connection = None
        self.controller = controller
        self.connect_odb()
        self.side_menu_visible = False
        self.side_menu_container = tk.Frame(master=self, bg='#282a36')
        b1 = tk.Button(self.side_menu_container)
        self.menu_button = tk.Button(self, justify=tk.LEFT, borderwidth=0, command=self.toggle_side_meu)
        b1.grid(row=0, column=0, padx=10, pady=10)
        self.side_menu_container.grid(row=0, column=1, padx=10, pady=10)

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
        self.test_gauge = Gauge.Gauge(self, 0, 100, 10, 1)

    def toggle_side_meu(self):
        self.side_menu_visible = not self.side_menu_visible
        if self.side_menu_visible:
            self.side_menu_container.pack()
        else:
            self.side_menu_container.pack_forget()
