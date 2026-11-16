import wave
import numpy as np

def extract_message(stego_wav: str) -> str:
    with wave.open(stego_wav, 'rb') as w:
        frames = w.readframes(w.getnframes())
    samples = np.frombuffer(frames, dtype=np.int16)

    bits = ''.join(str(s & 1) for s in samples)
    chars = [chr(int(bits[i:i+8], 2)) for i in range(0, len(bits), 8)]
    message = ''.join(chars).split(chr(0))[0]
    return message
