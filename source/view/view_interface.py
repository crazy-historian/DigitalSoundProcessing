import abc


class IView(abc.ABC):

    def start_recording(self, *args, **kwargs) -> None:
        """
            Receiving an event from View and initializing an audio recording
        """
        ...

    def stop_recording(self, *args, **kwargs) -> None:
        """
            Receiving an event and finish audio recording
        """
        ...

    def receive_output_from_model(self, *args, **kwargs) -> None:
        """
            Receiving and processing returned from model outputs of DSP methods
        """
        ...

    def execute_in_thread(self, function, **func_args) -> None:
        """
            Passed function works in new thread

        """
        ...

    def execute_in_process(self, function, **func_args) -> None:
        """
            Passed function works in new process
        """
        ...
