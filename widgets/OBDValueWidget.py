import tkinter as tk
import obd


class OBDValueWidget:

    def __init__(self, frame, cmd):
        self.cmd = cmd
        label = tk.Label(frame, text=cmd.name + ": ", font=("Helvetica", 14), fg="white")
        label['bg'] = label.master['bg']
        label.grid(row=0, column=0)
        self.value_label = tk.Label(frame, text="0", font=("Helvetica", 14), fg="white")
        self.value_label['bg'] = label.master['bg']
        self.value_label.grid(row=0, column=1)
        self.connection = obd.Async()
        self.connection.watch(self.cmd, callback=self.update_value)
        self. connection.start()

    def update_value(self, response):
        self.value_label.config(text=response.value)

    def stop_widget(self):
        self.connection.stop()
