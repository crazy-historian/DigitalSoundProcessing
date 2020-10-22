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
        # there will be a complex procedure of methods_dict initialising,
        # which will depends on View Interface
        methods = {
            "RMS": self.model.getRMS
        }
        self.audioRecording(methods=methods, time_in_sec=time_in_sec)

    def audioRecording(self, methods, time_in_sec=None):
        if time_in_sec is None:
            iterations = float('inf')
        else:
            iterations = self.model.getIterations(time_in_sec)
        iteration_num = 0

        while self.recording and iteration_num < iterations:
            iterations += 1
            outputs = {}
            self.model.readStream()
            for name in methods:
                outputs[name] = methods[name]()
            self.view.showModelData(outputs)
            self.view.newProcess()

    def stopRecord(self):
        self.model.closeStream()
        self.recording = False

