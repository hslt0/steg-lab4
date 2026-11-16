import wave
import numpy as np

def embed_message(input_wav: str, output_wav: str, message: str):
    message += chr(0)
    bits = ''.join(f'{ord(c):08b}' for c in message)

    with wave.open(input_wav, 'rb') as w:
        params = w.getparams()
        frames = w.readframes(params.nframes)
    samples = np.frombuffer(frames, dtype=np.int16)

    if len(bits) > len(samples):
        raise ValueError("Повідомлення занадто довге для цього аудіо")

    samples_mod = samples.copy()
    for i, bit in enumerate(bits):
        samples_mod[i] = (samples_mod[i] & ~1) | int(bit)

    with wave.open(output_wav, 'wb') as w:
        w.setparams(params)
        w.writeframes(samples_mod.tobytes())

    print(f"Повідомлення сховано в {output_wav}")