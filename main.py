from pyaudio import paInt16
from src.prcs.audio_stream import AudioChunk

chunk = AudioChunk(22400, 60, 1, paInt16)
chunk.open_stream()
chunk.design_butter_filter()
data = chunk.get_filtered_data()
print(data)
chunk.close_stream()
