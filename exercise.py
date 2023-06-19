from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.core.audio import SoundLoader
from kivy.properties import NumericProperty, StringProperty
from kivy.clock import Clock

Builder.load_file("kv/exercise.kv")


class Exercise(Screen):
    length = NumericProperty(0.0)
    progress = NumericProperty(0.0)
    timer = StringProperty()
    seconds = NumericProperty()
    minutes = NumericProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sound = SoundLoader.load("sounds/test.ogg")
        self.sound_position = None
        self.timer = "00:00"

    def play(self):
        """Äänen toistofunktio"""
        if self.sound:
            self.length = self.sound.length
            self.sound.play()
            # päivitetään  palkki sekunnin välein
            self.bar_progress = Clock.schedule_interval(self.update_progress_bar, 1.0)
            self.timer_progress = Clock.schedule_interval(self.string_time, 1.0)
            print("kuuluu ääniä!")
        else:
            print("äänen toisto ei onnistu T_T")

    def stop(self):
        self.sound.stop()
        print("ääni lopetettu!")
        self.progress = 0  # nollataan palkki
        self.timer = "00:00"
        self.seconds = 0
        self.minutes = 0
        self.bar_progress.cancel()
        self.timer_progress.cancel()

    def update_progress_bar(self, dt):  # ei toimi ilman kahta dt=datetime?
        if self.progress < self.length:
            self.progress += 1
        else:
            self.progress = 0  # nollataan palkki
            self.bar_progress.cancel()  # lopetataan päivittäminen

    def string_time(self, dt):
        self.update_seconds()
        seconds = str(self.seconds)
        minutes = str(self.minutes)

        if len(seconds) < 2:
            seconds = f"0{seconds}"

        if len(minutes) < 2:
            minutes = f"0{minutes}"

        self.timer = f"{minutes}:{seconds}"

    def update_seconds(self):
        if self.progress < self.length:
            self.seconds += 1

            if self.seconds == 60:
                self.update_minutes()
                self.seconds = 0

        else:
            self.seconds = 0
            self.minutes = 0
            self.timer_progress.cancel()

    def update_minutes(self):
        self.minutes += 1

    def on_start(self):
        self.timer = "00:00"


class Progress_bar:
    pass


class Timer:
    pass
