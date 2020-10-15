from audio_recording import Audio


class Presenter:
    def __init__(self, view):
        self.audio_model = Audio()
        self.view = view

    def startRecord(self, record_dict):
        self.audio_model.initStream(record_dict)
        self.audioProcessing()

    def audioProcessing(self, time=None, function=None):
        self.audio_model.readStream()
        rms = self.audio_model.getRMS()
        self.view.showModelData(rms)

    def stopRecord(self):
        self.audio_model.closeStream()
