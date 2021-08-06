from os.path import join

import numpy as np
import pydub
import sounddevice as sd


def clean_filename(f: str):
    while len(f) > 1 and f[0] in "0123456789_ ":
        f = f[1:]
    return f.replace("_", " ")


# https://stackoverflow.com/questions/53633177/how-to-read-a-mp3-audio-file-into-a-numpy-array-save-a-numpy-array-to-mp3
def read_audio(f, normalized=False):
    """MP3 to numpy array"""
    a = pydub.AudioSegment.from_mp3(f)
    y = np.array(a.get_array_of_samples())
    if a.channels == 2:
        y = y.reshape((-1, 2))
    if normalized:
        return a.frame_rate, np.float32(y) / 2 ** 15
    else:
        return a.frame_rate, y


class AudioFile:
    def __init__(self, name: str, path: str):
        self.name = name
        self.path = path

    def location(self):
        return str(join(self.path, self.name))

    def __repr__(self):
        return clean_filename('.'.join(self.name.split('.')[:-1]))

    def play(self):
        sampling_rate, signal = read_audio(self.location())
        sd.play(signal, samplerate=sampling_rate, blocking=False)
