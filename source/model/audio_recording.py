import pyaudio
import audioop


class Audio(pyaudio.PyAudio):

    def __init__(self):
        super().__init__()
        self.stream = None
        self.raw_data = None
        #
        self.rate = None
        self.chunk_size = None
        self.channels = None

    def configure_audio(self, audio_configuring):
        self.rate = audio_configuring["rate"]
        self.chunk_size = audio_configuring["chunk"]
        self.channels = audio_configuring["channel"]

    def init_stream(self):
        self.stream = self.open(
            format=pyaudio.paInt16,
            input=True,
            rate=self.rate,
            channels=self.channels,
            frames_per_buffer=self.chunk_size
        )

    def read_stream(self):
        if self.stream:
            self.chunk = self.stream.read(self.chunk_size)

    def get_rms(self):
        rms = audioop.rms(self.chunk, 2)
        return rms

    def get_iterations(self, seconds):
        return int((self.rate / self.chunk_size) * seconds)

    def close_stream(self):
        if self.stream is not None:
            self.stream.close()
            self.stream = None
            self.rate = None
            self.chunk_size = None
            self.channels = None

