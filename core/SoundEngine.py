from os import listdir

import sounddevice as sd

from config.settings import audio_directory, default_output_audio_device
from core.AudioFile import AudioFile


def set_sound_device(device: int = None):
    if not device:
        print(sd.query_devices())
        device = input("Set sound device:")
    try:
        sd.default.device[1] = int(device)
    except ValueError:
        print("Number not recognized, using default device instead")
    for d, s in zip([sd.query_devices()[x].get('name') for x in sd.default.device],
                    ["Input devce: {}", "Output device: {}.11.10"]):
        print(s.format(d))


class SoundEngine:
    def __init__(self, directory: str = audio_directory):
        self.directory = directory
        set_sound_device(device=default_output_audio_device)
        self.files = self.load_files()

    def load_files(self):
        file_names = [AudioFile(f, self.directory) for f in listdir(self.directory) if f.endswith('.mp3')]
        print('Loaded audio files:')
        for i, f in enumerate(file_names):
            print("{}: {}".format(i + 1, f))
        return file_names

    def play(self, nr: int = 1):
        nr -= 1
        if nr >= len(self.files):
            return
        try:
            self.files[nr].play()
        except Exception as e:
            print("Coulcn't play audio:", e)

    @staticmethod
    def stop_playing():
        sd.stop(ignore_errors=True)
