import tkinter as tk
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class VolumeConfigure(tk.Tk):
    def __init__(self):
        super().__init__()
        self.counter = 0
        self.data = 0
        self.x_axis = []
        self.y_axis = []
        self.min = 0
        self.max = 0
        self.callback = None
        self.font = "Consolas 32"
        # *******************
        self.figure = Figure(figsize=(5, 5), dpi=100)
        self.instant_plot = self.figure.add_subplot(111)
        self.instant_plot.plot(self.x_axis, self.y_axis)
        self.label = tk.Label(self, text=str(self.data), font=self.font)
        self.button = tk.Button(self, text="Установить значения min и max", font="Consolas 16", command=self.insert)
        self.min_entry = tk.Entry(self, font=self.font)
        self.max_entry = tk.Entry(self, font=self.font)
        self.canvas = FigureCanvasTkAgg(self.figure, self)

    def draw_plot(self, callback=None):
        if callback:
            self.data = callback()
            print(self.data)
            self.counter += 1

            self.y_axis.append(self.data)
            if len(self.y_axis) < 150:
                self.x_axis.append(self.counter)
            else:
                self.y_axis.pop(0)

            self.instant_plot.clear()
            self.instant_plot.set_ylim(0, max(self.y_axis))
            self.instant_plot.plot(self.x_axis, self.y_axis)

            self.canvas.draw()
            self.canvas.get_tk_widget().grid(row=0, column=0)
            self.label['text'] = "Громкость: " + str(round(np.mean(self.y_axis)))

    def loop(self):
        self.draw_plot(self.callback)
        self.after(10, self.loop)

    def pack(self):
        self.canvas.get_tk_widget().grid(row=0, column=0)
        self.label.place(x=0, y=500, width=500, height=50)
        self.min_entry.place(x=0, y=560, width=250, height=50)
        self.max_entry.place(x=255, y=560, width=250, height=50)
        self.button.place(x=0, y=620, width=500, height=50)

    def insert(self):
        self.min = int(self.min_entry.get())
        self.max = int(self.max_entry.get())
