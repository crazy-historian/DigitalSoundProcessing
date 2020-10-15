class Audio:

    def __init__(self):
        self.data = 100

    def initStream(self, record_dict):
        print("Audio:")
        for characteristic, value in record_dict.items():
            print(f"{characteristic}: {value}")
        return self.data
