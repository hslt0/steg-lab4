import wave
import numpy as np

from prng_utils import generate_indices


def extract_message_prng(stego_wav: str, key: str) -> str:
    with wave.open(stego_wav, "rb") as wav_file:
        frames = wav_file.readframes(wav_file.getnframes())
    samples = np.frombuffer(frames, dtype=np.int16)
    indices = generate_indices(key, len(samples))

    message_bytes = bytearray()
    for start in range(0, len(indices) - 7, 8):
        byte = 0
        for index in indices[start:start + 8]:
            byte = (byte << 1) | (int(samples[index]) & 1)
        if byte == 0:
            return message_bytes.decode("utf-8")
        message_bytes.append(byte)

    raise ValueError("Не знайдено кінець повідомлення: перевірте ключ і WAV-файл")
