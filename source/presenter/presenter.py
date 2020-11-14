from audio_recording import Audio
from PyQt5.QtWidgets import QApplication


class Presenter:
    def __init__(self, view=None):
        self.model = Audio()
        self.recording = False
        self.view = view

    def start_recording(self, audio_configuring, time_in_sec=None):
        self.model.configure_audio(audio_configuring)
        self.model.init_stream()
        self.recording = True
        # there will be a complex procedure of methods_dict initialising,
        # which will depends on View Interface
        methods = {
            "RMS": self.model.get_rms
        }
        self.view.execute_in_thread(self.audio_recording, methods=methods, time_in_sec=time_in_sec)

    def audio_recording(self, methods, time_in_sec):
        if time_in_sec is None:
            iterations = float('inf')
        else:
            iterations = self.model.get_iterations(time_in_sec)
            print(iterations)
        iteration_num = 0

        while self.recording and iteration_num < iterations:
            iteration_num += 1
            outputs = {}
            self.model.read_stream()
            for name in methods:
                outputs[name] = methods[name]()
            self.view.receive_output_from_model(outputs)
        else:
            self.stop_recording()
            self.model.close_stream()

    def stop_recording(self):
        self.recording = False



