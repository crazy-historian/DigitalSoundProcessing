from audio_recording import Audio


class Presenter:
    def __init__(self, view):
        self.audio_model = Audio()
        self.view = view

    def startRecord(self, record_dict):
        print("Presenter has got the signal from GUI")
        test_variable = self.audio_model.initStream(record_dict)
        self.view.showModelData(test_variable)
