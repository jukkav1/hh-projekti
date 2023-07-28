from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.core.audio import SoundLoader
from kivy.properties import NumericProperty, StringProperty
from kivy.clock import Clock

Builder.load_file("kv/exercise.kv")


class Exercise(Screen):
    length = NumericProperty(0.0)
    general_progress=NumericProperty(0.0)
    progress1 = NumericProperty(0.0)
    progress2 = NumericProperty(0.0)
    timer1 = StringProperty("00:00")
    timer2 = StringProperty("00:00")
    seconds = NumericProperty()
    minutes = NumericProperty()
    mika_nappi = 0
    audio_playing=False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def Button1(self, soundfile):
        # print("def Button1 kutsuttiin")
        self.sound = SoundLoader.load(soundfile)
        self.mika_nappi = 1
        # print(f"mika_nappi{self.mika_nappi}")

        if self.sound:
            if self.audio_playing==False:
                self.audio_playing=True
                print(f"audio_playing={self.audio_playing}")
                print("äänet löytyy")
                self.sound.play()
                self.audio_playing = True
                # print(f"audio_playing{self.audio_playing}")
                self.length = self.sound.length
                # print(f"lenght{self.length}")

                self.bar_progress = Clock.schedule_interval(self.update_progress_bar, 1.0)
                self.timer_progress = Clock.schedule_interval(self.string_time, 1.0)
        else:
            print("ei ole ääntä")
                

    def Button2(self, soundfile):
        # print("def Button2 kutsuttiin")
        self.sound = SoundLoader.load(soundfile)
        self.mika_nappi = 2
        # print(f"mika_nappi{self.mika_nappi}")

        if self.sound:
            
            
            # print("äänet löytyy")
            self.sound.play()
            # print(f"sound{self.sound}")
            self.audio_playing = True
            # print(f"audio_playing{self.audio_playing}")
            self.length = self.sound.length
            # print(f"lenght{self.length}")
            self.bar_progress = Clock.schedule_interval(self.update_progress_bar, 1.0)
            self.timer_progress = Clock.schedule_interval(self.string_time, 1.0)
    
    def stop_audio(self):
        if self.audio_playing==True:
            self.audio_playing=False
            print(f"audio_playing={self.audio_playing}")
            self.clear_time()
            self.sound.stop()
            print("ääni seisautettu")

    def clear_time(self):
        print(f"Koitetaan nollata nappi {self.mika_nappi}")
        self.timer_progress.cancel()
        self.bar_progress.cancel()
        self.timer1 = ("00:00")
        self.timer2 = ("00:00")
        self.progress1 = 0
        self.progress2 = 0
        self.seconds=0
        self.minutes=0
        self.general_progress=0
        

    def update_progress_bar(self, dt):
        # print("update progress bar kutsuttiin")

        if self.general_progress < self.length:
            self.general_progress += 1
            # print(f"progress:{self.progress_bar}")

        else:
            self.general_progress = 0
            # print(f"progress:{self.progress_bar}")
            self.bar_progress.cancel()

        if self.mika_nappi == 1:
            self.progress1 = self.general_progress

        elif self.mika_nappi == 2:
            self.progress2 = self.general_progress

    def string_time(self, dt):
        self.update_seconds()
        seconds = str(self.seconds)
        minutes = str(self.minutes)

        if len(seconds) < 2:
            seconds = f"0{seconds}"

        if len(minutes) < 2:
            minutes = f"0{minutes}"

        aika = f"{minutes}:{seconds}"

        if self.mika_nappi == 1:
            self.timer1 = aika
        elif self.mika_nappi == 2:
            self.timer2 = aika

    def update_seconds(self):
        if self.general_progress < self.length:
            self.seconds += 1

            if self.seconds == 60:
                self.update_minutes()
                self.seconds = 0
        else:
            self.seconds = 0
            self.minutes = 0
            self.timer_progress.cancel()
            self.audio_playing=False
            print(f"audio_playing={self.audio_playing}")

    def update_minutes(self):
        self.minutes += 1
