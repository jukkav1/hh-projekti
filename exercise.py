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
    audio_playing = False
    pause_pushed = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sound = SoundLoader.load("sounds/test.ogg")
        # self.sound = SoundLoader.load("sounds/mixkit-evil-storm-atmosphere-2404.wav")
        self.timer = "00:00"

    # vaatii vielä kikkailua jos audio soi loppuun ilman että pausettaa
    def play_stop_audio(self):
        if self.sound:
            if self.audio_playing == True:
                self.sound.stop()
                self.audio_playing = False
                self.progress = 0
                self.timer = "00:00"
                self.seconds = 0
                self.minutes = 0
                self.bar_progress.cancel()
                self.timer_progress.cancel()
                print(
                    f"äänet kuoli. self.audio_playing={self.audio_playing}"
                )
                self.update_icon()

            elif self.audio_playing == False:
                self.sound.play()
                self.audio_playing = True
                self.length = self.sound.length
                # clock_shedule_interval määrittää miten usein palkki/timer päivitetään
                self.bar_progress = Clock.schedule_interval(
                    self.update_progress_bar, 1.0
                )
                self.timer_progress = Clock.schedule_interval(self.string_time, 1.0)
                self.update_icon()
                print(f"kuuluu ääniä! self.audio_playing={self.audio_playing}")
            # else elif jos audio soi loppuun

        else:
            print("äänen toisto ei onnistu T_T")

    def update_icon(self):
        if self.ids.play_stop_btn.icon == "play":
            self.ids.play_stop_btn.icon = "pause"
        else:
            self.ids.play_stop_btn.icon = "play"

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
