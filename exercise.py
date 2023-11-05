# Copyright (c) 2023 Taru Haapala
# Copyright (c) 2023 Jukka Valvanne

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.core.audio import SoundLoader
from kivy.properties import NumericProperty, ListProperty
from kivy.clock import Clock

Builder.load_file("kv/exercise.kv")

# TODO:
# set_stop_buttons ja set_play_buttons riippuu edelleen kovakoodatun nappuloiden määrästä kv:n puolella (self.ids..); voiko for-loopilla käydä läpi?


class Exercise(Screen):
    s = "sounds"

    # fmt: off
    # tämä sanakirja sisältää äänitiedostojen tiedot:
    # nimi | suhteellinen polku | aika | aika sekunteina
    sdict = [
        {"name": "Metsä", "file": f"{s}/ambient_forest_new.mp3", "time": "08:12", "length": 492},
        {"name": "Lehdet", "file": f"{s}/lehdet.mp3", "time": "07:52", "length": 472},
        {"name": "Sade", "file": f"{s}/sade.mp3", "time": "07:54", "length": 474},
        {"name": "Lintuääni", "file": f"{s}/test.ogg", "time": "00:04", "length": 4}
        ]
    # fmt: on
    sdlength = len(sdict)

    # ajastimet ja etenemispalkit audioraidoille
    bar_progresses = ListProperty([0] * sdlength)
    timers = ListProperty(["00:00"] * sdlength)

    # määritetään tarvittavia muuttujia
    general_progress = NumericProperty(0.0)
    seconds = NumericProperty()
    minutes = NumericProperty()

    # aloitetaan audio ja asetetaan arvo pressed_button muuttujalle
    def play_audio(self, pressed_btn: int):
        """kivyn puolen napit kutsuu tätä (on_release:root.play_audio(x,y))"""
        # ladataan äänitiedosto
        soundfile = self.sdict[pressed_btn - 1]["file"]
        self.sound = SoundLoader.load(soundfile)
        self.pressed_button = pressed_btn

        # Jos ääni löytyy ..
        # fmt: off
        if self.sound:
            print(f"ääni {soundfile} napista {self.pressed_button} löytyy")
            self.sound.play()
            #fmt: on

            # togletaan play:disable / stop:enable,  jos jokin ääni ON JO KÄYNNISSÄ
            self.toggle_buttons()

            # käynnistetään kello jotta latauspalkki ja ajasti lähtee pyörimään, määritetään kuinka usein päivitetään(tässä sekunnin välein)
            # tehdään kellosta samalla muuttuja, jolla  kellon toiminnan voi sitten myöhemmin lopettaa (.cancel())
            self.bar_progress = Clock.schedule_interval(self.update_progress_bar, 1.0)
            self.timer_progress = Clock.schedule_interval(self.string_time, 1.0)
        else:
            print("ei ole ääntä")

    def toggle_buttons(self):
        """Toggles wether the play / stop buttons are enabled or disabled. based on play_one value"""
        setting = self.ids.play_one.disabled
        self.set_play_buttons(not setting)
        self.set_stop_buttons(setting)

    def set_play_buttons(self, setting: bool):
        """Toggle play buttons by bool"""
        self.ids.play_one.disabled = setting
        self.ids.play_two.disabled = setting
        self.ids.play_three.disabled = setting
        self.ids.play_four.disabled = setting

    def set_stop_buttons(self, setting: bool):
        """Toggle stop buttons by bool"""
        self.ids.stop_one.disabled = setting
        self.ids.stop_two.disabled = setting
        self.ids.stop_three.disabled = setting
        self.ids.stop_four.disabled = setting

    def stop_audio(self):
        """Pysäyttää audion"""
        # play napit takaisin käyttöön
        self.toggle_buttons()
        self.clear_time()

        # pysäytetään audio
        self.sound.stop()
        print("ääni pysäytetty")

    def clear_time(self):
        """Nollaa kellot, ajat, palkit ja muuttujat"""
        # nollaa kellot
        self.timer_progress.cancel()
        self.bar_progress.cancel()

        # ajastimet
        for _ in range(len(self.timers)):
            self.timers[_] = "00:00"

        # palkit
        for _ in range(len(self.bar_progresses)):
            self.bar_progresses[_] = 0

        # muuttujat
        self.seconds = 0
        self.minutes = 0
        self.general_progress = 0

    def update_progress_bar(self, dt):
        """Etenemispalkin päivitystoiminnot"""
        if self.general_progress < self.sound.length:
            self.general_progress += 1

        else:
            # jos aika on täysi, nollaa ja pysäytä äänet ja palkit.
            self.general_progress = 0
            self.bar_progress.cancel()
            self.stop_audio()

        # joka tapauksessa päivitä palkki
        self.bar_progresses[self.pressed_button - 1] = self.general_progress

    def string_time(self, dt):
        """ajasta muodostetaan labelille sopiva muoto ja päivitellään sitä"""
        self.update_seconds()

        # Kivyn label hyväksyy vain merkkijonoja.
        seconds = str(self.seconds)
        minutes = str(self.minutes)

        # saadaan time päivittymään oikean näköisena kv puolelle
        # lisää "puuttuvan" nollan aikamerkintään; 00:00
        if len(seconds) < 2:
            seconds = f"0{seconds}"

        if len(minutes) < 2:
            minutes = f"0{minutes}"

        time = f"{minutes}:{seconds}"

        # minne aikatieto tallennetaan
        self.timers[self.pressed_button - 1] = time

    def update_seconds(self):
        """sekunnin päivitys"""
        if self.general_progress < self.sound.length:
            self.seconds += 1

            # jos sekunnit 60, lisää minuutti ja nollaa sekunnit
            if self.seconds == 60:
                self.minutes += 1
                self.seconds = 0

        else:
            # pysäytetään kello
            self.timer_progress.cancel()

            # asetetaan play napit takasin käyttöön jos audio soi loppuun ja nollataan aika
            self.toggle_buttons()
            self.clear_time()
