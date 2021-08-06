from pynput.keyboard import Listener, Key

from core.SoundEngine import SoundEngine

modifiers_keys = [Key.alt_gr, Key.alt_l, Key.shift_l, Key.shift_r, Key.ctrl_l, Key.ctrl_r]


class KeyListener(Listener):
    def __init__(self, sound_engine: SoundEngine):
        self.sound = sound_engine
        self.modifiers = {k: False for k in modifiers_keys}
        self.long_input = [False, 0]
        super(KeyListener, self).__init__(on_press=self.key_press_event, on_release=self.key_release_event)

    def key_press_event(self, key):
        if key in modifiers_keys:
            self.modifiers[key] = True
            return
        if any(self.modifiers.values()):
            return
        # print(key)

        # Key functions
        if key.char == 'r' and self.long_input[0]:
            self.sound.load_files()
            return

            # Key functions with irregular keys
        if not hasattr(key, 'vk'):
            return
        # Numpad 0-9
        if 96 <= key.vk <= 105:
            if key.vk == 96 and not self.long_input[0]:
                self.sound.stop_playing()
                return
            sound_nr = key.vk - 96
            if self.long_input[0]:
                self.long_input[1] = self.long_input[1] * 10 + sound_nr
            else:
                self.sound.play(sound_nr)
            return
        if key.vk == 110:
            self.long_input[0] = True

    def key_release_event(self, key):
        if key in modifiers_keys:
            self.modifiers[key] = False
            return

        # Key functions with irregular keys
        if not hasattr(key, 'vk'):
            return
        # Numpad .
        if key.vk == 110:
            if self.long_input[1] > 0:
                self.sound.play(self.long_input[1])
                self.long_input = [False, 0]
            return
