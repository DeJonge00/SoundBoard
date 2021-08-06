from core.KeyListener import KeyListener
from core.SoundEngine import SoundEngine


def main():
    sound = SoundEngine()
    with KeyListener(sound_engine=sound) as listener:
        listener.join()

    for s in sound.files:
        s.play()


if __name__ == "__main__":
    main()
