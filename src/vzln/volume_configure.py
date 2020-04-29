import tkinter as tk
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from prcs.audio_stream import AudioChunk


class VolumeConfigure(tk.Tk):
    def __init__(self, fps=None,
                 input_callback=None,
                 processing_callback = None,
                 output_callback=None):
        super().__init__()
        # plot
        self.x_axis = np.array([], np.int16)
        self.y_axis = np.array([], np.float)
        self.counter = 0
        self.data = 0
        self.figure = Figure(figsize=(5, 5), dpi=100)
        self.instant_plot = self.figure.add_subplot(111)
        self.instant_plot.set_ylabel("Volume level, RMS")
        self.instant_plot.set_ylabel("Time, RMS")
        # interface
        self.min = 0
        self.max = 0
        self.read_stream = input_callback
        self.get_volume = processing_callback
        self.output = output_callback
        # tk widgets
        self.font = "Consolas 32"
        self.fps = fps
        self.rate_ms = 1000 // self.fps
        self.label = tk.Label(self, text=str(self.data), font=self.font)
        self.button = tk.Button(self, text="Установить значения min и max", font="Consolas 16", command=self.insert)
        self.min_entry = tk.Entry(self, font=self.font)
        self.max_entry = tk.Entry(self, font=self.font)
        self.canvas = FigureCanvasTkAgg(self.figure, self)

    def draw_plot(self):
        if self.read_stream:
            self.read_stream()
            self.data = self.get_volume()
            self.counter += 1

            self.y_axis = np.append(self.y_axis, self.data)
            if len(self.y_axis) <= self.fps:
                self.x_axis = np.append(self.x_axis, self.counter)
            else:
                self.y_axis = np.delete(self.y_axis, 0)

            current_max = np.amax(self.y_axis)
            if self.max < current_max:
                self.max = current_max

            self.instant_plot.clear()
            self.instant_plot.set_ylim(0, self.max)
            self.instant_plot.plot(self.x_axis, self.y_axis)

            self.canvas.draw()
            self.canvas.get_tk_widget().grid(row=0, column=0)
            self.label['text'] = f"Громкость:{round(np.mean(self.y_axis, axis=0))} "

    def loop(self):
        self.draw_plot()
        self.after(self.rate_ms, self.loop)

    def pack(self):
        self.canvas.get_tk_widget().grid(row=0, column=0)
        self.label.place(x=0, y=500, width=500, height=50)
        self.min_entry.place(x=0, y=560, width=250, height=50)
        self.max_entry.place(x=255, y=560, width=250, height=50)
        self.button.place(x=0, y=620, width=500, height=50)

    def insert(self):
        self.min = int(self.min_entry.get())
        self.max = int(self.max_entry.get())
