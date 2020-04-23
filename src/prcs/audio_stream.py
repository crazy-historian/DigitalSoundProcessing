import pyaudio
import numpy as np
import audioop
from numpy import fft
from scipy.signal import butter, filtfilt


class AudioChunk(pyaudio.PyAudio):

    def __init__(self, rate, fps, channels, fr_format):
        super().__init__()
        self.rate = rate
        self.fps = fps
        self.chunk = rate // fps // 2
        self.channels = channels
        self.fr_format = fr_format
        self.stream = None
        self.input_device_index = None

        # filter requirements
        self.a = None
        self.b = None

    def check_input_device(self):
        print("Default device:", self.get_default_input_device_info())
        try:
            # TODO: gui sub window to choose index
            for i in range(self.get_device_count()):
                print("Device number (%i): %s" % (i, self.get_device_info_by_index(i).get('name')))
        except IOError:
            raise Exception("Отсутствует микрофон")

    def open_stream(self):
        self.stream = self.open(format=self.fr_format, channels=self.channels, rate=self.rate,
                                input=True, frames_per_buffer=self.chunk, )

    def get_raw(self):
        raw_data = self.stream.read(self.chunk, exception_on_overflow=False)
        return raw_data

    def get_unpacked_raw(self):
        int_data = np.frombuffer(self.get_raw(), np.int16).astype(np.float)
        return int_data

    def get_rms_from_raw(self):
        rms = audioop.rms(self.get_raw(), 2)
        return rms

    def get_rms_from_unpacked(self):
        rms = np.sqrt(np.mean(self.get_unpacked_raw() ** 2))
        return rms

    def design_butter_filter(self, lowcut=500, highcut=900, order=3):
        nyq_freq = 0.5 * self.rate
        low = lowcut / nyq_freq
        high = highcut / nyq_freq
        self.b, self.a = butter(order, low, btype='low', analog=False)
        return self.b, self.a

    def get_filtered_data(self):
        unpacked_raw = self.get_unpacked_raw()
        print(np.sqrt(np.mean(unpacked_raw ** 2)))
        filtered_data = filtfilt(self.b, self.a, unpacked_raw)
        print(np.sqrt(np.mean(filtered_data ** 2)))
        return filtered_data

    def get_fft(self):
        data = self.get_unpacked_raw()
        print(data)
        n = len(data)
        d = 1 / self.rate
        hs = fft.rfft(data)
        fs = fft.rfftfreq(n, d)
        return hs, fs

    def close_stream(self):
        self.stream.close()
