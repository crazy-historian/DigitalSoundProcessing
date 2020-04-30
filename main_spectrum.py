from pyaudio import paInt16
from src.prcs.audio_stream import AudioChunk
from src.vzln.spectrogram import Spectrogram

audio = AudioChunk(22400, 20, 1, paInt16)
audio.open_stream()
audio.design_butter_filter()
spectrogram = Spectrogram(20, audio)
spectrogram.pack()

spectrogram.after_idle(spectrogram.loop)
spectrogram.after(2000000, spectrogram.destroy)
spectrogram.mainloop()
audio.close_stream()
