import librosa
import numpy as np
import glob
import os
import sys
for infile in glob.glob("*.wav"):
    filename = infile
    y, sr = librosa.load(filename, sr=16000)

    mel_spectrogram = librosa.feature.melspectrogram(
        y=y, sr=sr, n_mels=128, n_fft=1024, hop_length=512, power=2)
    log_mel_spectrogram = 20.0 / 2 * np.log10(np.maximum(mel_spectrogram, sys.float_info.epsilon))
    np.save(filename+".npy", log_mel_spectrogram)
    print(sr)
