import wave
import numpy as np
import matplotlib.pyplot as plt

with wave.open('meow.wav', 'rb') as wavFile:
    #Зчитування метаданних з файлу
    if wavFile.getcomptype() == 'NONE':
        print("Encoding: PCM")
    else:
        print(f"Encoding: {wavFile.getcompname()}")

    if (wavFile.getnchannels() == 1):
        print("Channels: Mono")
    else:
        print("Channels: Stereo")

    print(f"Frame Rate: {wavFile.getframerate() / 1000} Hz")

    print(f"Bit Depth: {wavFile.getsampwidth() * 8}-bit")

    #Зчитування перших 100 фреймів
    print(f"First 100 Frames: {wavFile.readframes(100)}")

    #Отримання з фреймів амплітуди сигналу
    signal = np.frombuffer(wavFile.readframes(-1), np.int16)
    print(f"Amplitudes: {signal[:100]}")

#Візуалізація графіка звукової хвилі
plt.figure(figsize=(10, 4))
plt.plot(signal, color='b')
plt.title("Audio Wave")
plt.xlabel("Frames")
plt.ylabel("Amplitude")
plt.show()