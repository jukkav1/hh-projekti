from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

# äänien toistoa varten
from kivy.core.audio import SoundLoader


class Exercise(Screen):
    """harjoitukset"""

    Builder.load_file("kv/exercise.kv")

    def play_sound(self):
        """Äänen toistofunktio"""

        sound = SoundLoader.load("sounds/test.ogg")
        if sound:
            sound.play()
        else:
            print("äänen toisto ei onnistu T_T")
        pass
