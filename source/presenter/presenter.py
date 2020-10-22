from audio_recording import Audio
from PyQt5.QtWidgets import QApplication


class Presenter:
    def __init__(self, view=None):
        self.model = Audio()
        self.recording = False
        self.view = view

    def startRecord(self, audio_configuring, time_in_sec=None):
        self.model.configureAudio(audio_configuring)
        self.model.initStream()
        self.recording = True
        self.audioRecording(time_in_sec=time_in_sec)

    def audioRecording(self, time_in_sec=None):
        if time_in_sec is None:
            iterations = float('inf')
        else:
            iterations = self.model.getIterations(time_in_sec)
        iteration_num = 0

        while self.recording and iteration_num < iterations:
            iterations += 1
            self.model.readStream()
            rms = self.model.getRMS()
            self.view.showModelData(rms)
            self.view.newProcess()

    def stopRecord(self):
        self.model.closeStream()
        self.recording = False

