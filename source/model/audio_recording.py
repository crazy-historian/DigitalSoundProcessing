import pyaudio
import audioop


class Audio(pyaudio.PyAudio):

    def __init__(self):
        super().__init__()
        self.stream = None
        self.raw_data = None
        self.data = 100

    def initStream(self, record_dict):
        self.stream = self.open(
            format=pyaudio.paInt16,
            input=True,
            rate=record_dict['rate'],
            channels=record_dict['channel'],
            frames_per_buffer=record_dict['chunk']
        )

    def readStream(self):
        self.chunk = self.stream.read()

    def getRMS(self):
        rms = audioop.rms(self.chunk, 2)
        return rms

    def closeStream(self):
        self.stream.close()
