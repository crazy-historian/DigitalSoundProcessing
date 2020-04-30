import pyaudio
import numpy as np
import audioop
from numpy import fft
from scipy.signal import butter, filtfilt
from collections import namedtuple


class AudioChunk(pyaudio.PyAudio):

    def __init__(self, rate, fps, channels, fr_format):
        super().__init__()
        self.chunk = np.array([], bytes)
        self.rate = rate
        self.fps = fps
        self.chunk_size = self.rate // self.fps
        self.channels = channels
        self.fr_format = fr_format
        self.stream = None
        self.input_device_index = None

        # requirements for algorithms
        self.fft_tuple = namedtuple('FFT', 'amplitude frequency')
        self.low_odds = namedtuple('Low_odds', 'b a')
        self.band_odds = namedtuple('Band_odds', 'b a')
        self.high_odds = namedtuple('High_odds', 'b a')
        #
        self.low = None
        self.band = None
        self.high = None

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
                                input=True, frames_per_buffer=self.chunk_size, )

    def design_butter_filter(self, low_freq=150, high_freq=1500, order=5):
        nyq_freq = 0.5 * self.rate
        low = low_freq / nyq_freq
        high = high_freq / nyq_freq
        self.low = self.low_odds(*butter(order, low, btype='low', analog=False))
        self.band = self.band_odds(*butter(order, [low, high], btype='bandpass', analog=False))
        self.high = self.high_odds(*butter(order, high, btype='high', analog=False))

    def read_from_stream(self):
        self.chunk = self.stream.read(self.chunk_size, exception_on_overflow=False)

    def unpack(self):
        if isinstance(self.chunk, bytes):
            int_data = np.frombuffer(self.chunk, np.int16).astype(np.float)
            return int_data

    def get_rms_from_raw(self):
        if isinstance(self.chunk, bytes):
            rms = audioop.rms(self.chunk, 2)
            return rms

    def get_rms_from_int(self, unpacked=None):
        if unpacked is None:
            unpacked = self.unpack()
        rms = np.sqrt(np.mean(unpacked ** 2))
        return rms

    def get_filtered(self, ftype, data=None):
        if data is None:
            data = self.unpack()
        filtered_data = filtfilt(self.__dict__[ftype].b, self.__dict__[ftype].a, data)
        return filtered_data

    def get_fft(self, data=None):
        if data is None:
            data = self.unpack()
        n = len(data)
        d = 1 / self.rate
        hs = np.abs(fft.rfft(data))
        fs = fft.rfftfreq(n, d)
        transform = self.fft_tuple(amplitude=hs, frequency=fs)
        return transform

    def close_stream(self):
        self.stream.close()
