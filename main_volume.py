from pyaudio import paInt16
from src.prcs.audio_stream import AudioChunk
from src.vzln.volume_configure import VolumeConfigure

chunk = AudioChunk(22400, 20, 1, paInt16)
chunk.open_stream()
window = VolumeConfigure(fps=20,
                         input_callback=chunk.read_from_stream,
                         processing_callback=chunk.get_rms_from_raw)
window.geometry("500x670+100+100")
window.pack()

window.after_idle(window.loop)  # start loop
window.after(120000, window.destroy)  # quit in 5 seconds
window.mainloop()
chunk.close_stream()
