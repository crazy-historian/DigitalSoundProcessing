import tkinter as tk
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Spectrogram(tk.Tk):
    def __init__(self, fps, audio):
        super().__init__()
        # audio processing
        self.rate_ms = 1000 // fps
        self.audio = audio
        # plot
        self.figure = Figure(figsize=(15, 6), dpi=100)
        self.fft_plot = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, self)
        # tk widgets
        self.font = "Consolas 16"
        self.low_freq_widget = tk.Label(font=self.font, text="Low")
        self.band_freq_widget = tk.Label(font=self.font, text="Band")
        self.high_freq_widget = tk.Label(font=self.font, text="High")
        self.geometry("1500x800")

    def draw_plot(self):
        # audio processing
        self.audio.read_from_stream()
        data = self.audio.get_fft()
        low_data = self.audio.get_fft(self.audio.get_filtered(ftype="low"))
        band_data = self.audio.get_fft(self.audio.get_filtered(ftype="band"))
        high_data = self.audio.get_fft(self.audio.get_filtered(ftype="high"))
        #

        # plotting
        self.fft_plot.clear()
        self.fft_plot.set_ylim(0, 10000000)
        self.fft_plot.set_xlim(20, 22400/2)
        self.fft_plot.semilogx(data.frequency, data.amplitude, color='black', label='Original')
        self.fft_plot.semilogx(low_data.frequency, low_data.amplitude, color='red', label='Low pass')
        self.fft_plot.semilogx(band_data.frequency, band_data.amplitude, color='blue', label='Band pass')
        self.fft_plot.semilogx(high_data.frequency, high_data.amplitude, color='green', label='High pass')
        self.fft_plot.legend()

        self.canvas.draw()

    def pack(self):
        self.figure.canvas.get_tk_widget().grid(row=0, column=0)
        self.low_freq_widget.place(y=610, x=0, width=300, height=50)
        self.band_freq_widget.place(y=610, x=500, width=300, height=50)
        self.high_freq_widget.place(y=610, x=1000, width=300, height=50)

    def loop(self):
        self.draw_plot()
        self.after(self.rate_ms, self.loop)
