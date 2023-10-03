# Copyrighted under the MIT license, See LICENSE.
# Copyright (c) 2023 Jukka Valvanne & Taru Haapala

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.core.audio import SoundLoader
from kivy.properties import NumericProperty, StringProperty
from kivy.clock import Clock

Builder.load_file("kv/exercise.kv")


class Exercise(Screen):
    # määritetään tarvittavia muuttujia
    length = NumericProperty(0.0)  # määritetään tyyppi muuttujalle
    general_progress = NumericProperty(0.0)

    # etenemispalkkien arvot, viedään kv:lle (kivy language)
    bar_progress1 = NumericProperty(0.0)
    bar_progress2 = NumericProperty(0.0)
    bar_progress3 = NumericProperty(0.0)
    bar_progress4 = NumericProperty(0.0)

    # ajastimen arvot
    timer1 = StringProperty("00:00")
    timer2 = StringProperty("00:00")
    timer3 = StringProperty("00:00")
    timer4 = StringProperty("00:00")

    # sekunnit ja minuutit
    seconds = NumericProperty()
    minutes = NumericProperty()

    # apumuuttuja sille, mitä painiketta painettiin jotta voidaan käsitellä oikeaa audioraitaa
    pressed_button = 0

    # aloitetaan audio ja asetetaan arvo pressed_button muuttujalle
    def play_audio(self, soundfile: str, pressed_btn: int):
        """kivyn puolen napit kutsuu tätä (on_release:root.play_audio(x,y))"""
        # ladataan äänitiedosto
        self.sound = SoundLoader.load(soundfile)
        self.pressed_button = pressed_btn

        # Jos ääni löytyy ..
        if self.sound:
            print(f"ääni {soundfile} napista {self.pressed_button} löytyy")
            self.sound.play()

            # togletaan play:disable / stop:enable,  jos jokin ääni ON JO KÄYNNISSÄ
            self.toggle_buttons()

            # asetetaan arvo muuttujalle
            self.length = self.sound.length

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
        """Palautetaan muuttujat alkutilaan"""
        self.timer_progress.cancel()
        self.bar_progress.cancel()
        self.timer1 = "00:00"
        self.timer2 = "00:00"
        self.timer3 = "00:00"
        self.timer4 = "00:00"
        self.bar_progress1 = 0
        self.bar_progress2 = 0
        self.bar_progress3 = 0
        self.bar_progress4 = 0
        self.seconds = 0
        self.minutes = 0
        self.general_progress = 0

    def update_progress_bar(self, dt):
        """Etenemispalkin päivitystoiminnot"""
        if self.general_progress < self.length:
            self.general_progress += 1

        # latauspalkki nollautuu  toistaiseksi sekunnin myöhemmin kuin muut palat
        else:
            self.general_progress = 0
            # lopetaan kellon toiminta
            self.bar_progress.cancel()

            # stop audio heti jos timer käy loppuun
            self.stop_audio()

        # minne tiedot tallennetaan
        if self.pressed_button == 1:
            self.bar_progress1 = self.general_progress

        elif self.pressed_button == 2:
            self.bar_progress2 = self.general_progress

        elif self.pressed_button == 3:
            self.bar_progress3 = self.general_progress

        elif self.pressed_button == 4:
            self.bar_progress4 = self.general_progress

    def string_time(self, dt):
        """ajasta muodostetaan labelille sopiva muoto ja päivitellään sitä"""
        self.update_seconds()

        # time muutetaan sellaiseksi minkä kv puolen label ymmärtää
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
        if self.pressed_button == 1:
            self.timer1 = time
        elif self.pressed_button == 2:
            self.timer2 = time
        elif self.pressed_button == 3:
            self.timer3 = time
        elif self.pressed_button == 4:
            self.timer4 = time

    def update_seconds(self):
        """sekunnin päivitys"""
        if self.general_progress < self.length:
            self.seconds += 1

            # update_minutes() kutsutaan jos sekunnit enemmän kuin 60, samalla nollataaan sekunnit
            if self.seconds == 60:
                self.minutes += 1
                self.seconds = 0

        else:
            # nollataan  muuttujat
            self.seconds = 0
            self.minutes = 0

            # pysäytetään kello
            self.timer_progress.cancel()

            # asetetaan play napit takasin käyttöön jos audio soi loppuun ja nollataan aika
            self.toggle_buttons()
            self.clear_time()
