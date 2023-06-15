from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.core.audio import SoundLoader
from kivy.properties import NumericProperty
from kivy.clock import Clock

Builder.load_file("kv/exercise.kv")


class Exercise(Screen):
    length = NumericProperty(0.0)
    progress = NumericProperty(0.0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sound = SoundLoader.load("sounds/test.ogg")
        self.sound_position = None

    def play(self):
        """Äänen toistofunktio"""
        if self.sound:
            self.length = self.sound.length
            self.sound.play()
            # päivitetään  palkki sekunnin välein
            self.prog_ev = Clock.schedule_interval(self.update_progress, 1.0)
            print("kuuluu ääniä!")
        else:
            print("äänen toisto ei onnistu T_T")

    def stop(self):
        self.sound.stop()
        print("ääni lopetettu!")
        self.progress = 0  # nollataan palkki
        self.prog_ev.cancel()

    def update_progress(self, dt):  # ei toimi ilman kahta
        if self.progress < self.length:
            self.progress += 1 
        else:
            self.progress = 0  # nollataan palkki
            self.prog_ev.cancel()  # lopetataan päivittäminen
