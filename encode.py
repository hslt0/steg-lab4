import wave
import numpy as np

from prng_utils import generate_indices


def embed_message_prng(
    input_wav: str, output_wav: str, message: str, key: str
) -> None:
    payload = message.encode("utf-8") + b"\0"
    bits = np.unpackbits(np.frombuffer(payload, dtype=np.uint8))

    with wave.open(input_wav, "rb") as wav_file:
        params = wav_file.getparams()
        frames = wav_file.readframes(params.nframes)
    samples = np.frombuffer(frames, dtype=np.int16)

    if len(bits) > len(samples):
        raise ValueError("Повідомлення занадто довге для цього аудіо")

    indices = generate_indices(key, len(samples))[:len(bits)]
    samples_mod = samples.copy()
    samples_mod[indices] = (samples_mod[indices] & ~1) | bits

    with wave.open(output_wav, "wb") as wav_file:
        wav_file.setparams(params)
        wav_file.writeframes(samples_mod.tobytes())

    print(f"Повідомлення сховано в {output_wav} з використанням PRNG")