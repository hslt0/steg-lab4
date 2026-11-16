import wave
import numpy as np
import matplotlib.pyplot as plt

def plot_waveforms(wav1: str, wav2: str):
    def read_wav(path):
        with wave.open(path, 'rb') as w:
            sr = w.getframerate()
            frames = w.readframes(w.getnframes())
        data = np.frombuffer(frames, dtype=np.int16)
        time = np.linspace(0, len(data)/sr, num=len(data))
        return time, data

    t1, s1 = read_wav(wav1)
    t2, s2 = read_wav(wav2)

    plt.figure(figsize=(12, 6))
    plt.subplot(2,1,1)
    plt.plot(t1, s1)
    plt.title("Оригінал")
    plt.xlabel("Час (с)"); plt.ylabel("Амплітуда")

    plt.subplot(2,1,2)
    plt.plot(t2, s2, linestyle='--')
    plt.title("Стего")
    plt.xlabel("Час (с)"); plt.ylabel("Амплітуда")

    plt.tight_layout()
    plt.show()