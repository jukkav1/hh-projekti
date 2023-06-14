from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

# äänien toistoa varten
from kivy.core.audio import SoundLoader
from kivy.properties import NumericProperty
from kivy.clock import Clock

Builder.load_file("kv/exercise.kv")


class Exercise(Screen):
    def __init__(self, **kwargs):
        self.sound = SoundLoader.load("sounds/test.ogg")
        self.sound_position = None
        super().__init__(**kwargs)

    def play(self):
        self.sound.play()
        print("kuuluu ääniä!")

    def stop(self):
        self.sound.stop()
        print("ei kuulu ääniä!")


#    length = NumericProperty(0.0)
#    progress = NumericProperty(0.0)
#
#    def play_sound(self):
#        """Äänen toistofunktio"""
#        sound = SoundLoader.load("sounds/test.ogg")
#        if sound:
#            self.length = sound.length
#            sound.play()
#            # päivitetään sekunnin välein
#            self.prog_ev = Clock.schedule_interval(self.update_progress, 1.0)
#        else:
#            print("äänen toisto ei onnistu T_T")
#
#    def update_progress(self, dt):  # ei toimi ilman kahta
#        if self.progress < self.length:
#            self.progress += 1
#        else:
#            self.progress = 0  # nollataan palkki
#            self.prog_ev.cancel()  # lopetataan päivittäminen
#
