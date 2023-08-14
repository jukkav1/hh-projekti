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

    # etenemispalkkien arvot, viedään kv:lle
    bar_progress1 = NumericProperty(0.0)
    bar_progress2 = NumericProperty(0.0)
    bar_progress3 = NumericProperty(0.0)

    # ajastimen arvot
    timer1 = StringProperty("00:00")
    timer2 = StringProperty("00:00")
    timer3 = StringProperty("00:00")

    # sekunnit ja minuutit
    seconds = NumericProperty()
    minutes = NumericProperty()

    # apumuuttuja sille, mitä painiketta painettiin jotta voidaan käsitellä oikeaa audioraitaa
    mika_nappi = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # miten saadaan karsittua yhdeksi napiksi, niin että saadaan aina oikea audio päälle, pois?
    def Button1(self, soundfile: str):
        """1. nappulan play-nappula kutsuu tätä"""
        # ladataan äänitiedosto
        self.sound = SoundLoader.load(soundfile)
        self.mika_nappi = 1

        # Jos ääni löytyy ..
        if self.sound:
            print("äänet löytyy")
            self.sound.play()

            # otetaan play napit pois käytöstä jos jokin ääni ON JO KÄYNNISSÄ
            self.ids.play_one.disabled = True
            self.ids.play_two.disabled = True
            self.ids.play_three.disabled = True
            self.length = self.sound.length

            # käynnistetään kello jotta latauspalkki ja ajasti lähtee pyörimään, määritetään kuinka usein päivitetään(tässä sekunnin välein)
            self.bar_progress = Clock.schedule_interval(self.update_progress_bar, 1.0)
            self.timer_progress = Clock.schedule_interval(self.string_time, 1.0)
        else:
            print("ei ole ääntä")

    def Button2(self, soundfile: str):
        """2. nappulan toiminta."""

        self.sound = SoundLoader.load(soundfile)
        self.mika_nappi = 2

        if self.sound:
            print("äänet löytyy")
            # käynnistetää audio
            self.sound.play()
            self.ids.play_one.disabled = True
            self.ids.play_two.disabled = True
            self.ids.play_three.disabled = True
            # määritetään myöhempää käyttöä varten
            self.length = self.sound.length
            self.bar_progress = Clock.schedule_interval(self.update_progress_bar, 1.0)
            self.timer_progress = Clock.schedule_interval(self.string_time, 1.0)

    def Button3(self, soundfile: str):
        """3. nappulan funktio"""
        self.sound = SoundLoader.load(soundfile)
        self.mika_nappi = 3

        if self.sound:
            print("äänet löytyy")
            # käynnistetään audio
            self.sound.play()
            self.ids.play_one.disabled = True
            self.ids.play_two.disabled = True
            self.ids.play_three.disabled = True
            # määritetään myöhempää käyttöä varten
            self.length = self.sound.length
            self.bar_progress = Clock.schedule_interval(self.update_progress_bar, 1.0)
            self.timer_progress = Clock.schedule_interval(self.string_time, 1.0)

    def stop_audio(self):
        """Pysäyttää audion"""
        # play napit takaisin käyttöön
        self.ids.play_one.disabled = False
        self.ids.play_two.disabled = False
        self.ids.play_three.disabled = False
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
        self.bar_progress1 = 0
        self.bar_progress2 = 0
        self.bar_progress3 = 0
        self.seconds = 0
        self.minutes = 0
        self.general_progress = 0

    def update_progress_bar(self, dt):
        """Etenemispalkin päivitystoiminnot"""
        if self.general_progress < self.length:
            self.general_progress += 1

        else:
            self.general_progress = 0
            # lopetaan kellon toiminta
            self.bar_progress.cancel()

        # minne tiedot tallennetaan
        if self.mika_nappi == 1:
            self.bar_progress1 = self.general_progress

        elif self.mika_nappi == 2:
            self.bar_progress2 = self.general_progress

        elif self.mika_nappi == 3:
            self.bar_progress3 = self.general_progress

    def string_time(self, dt):
        """ajasta muodostetaan labelille sopiva muoto ja päivitellään sitä"""
        self.update_seconds()
        # aika muutetaan sellaiseksi minkä kv puolen label ymmärtää
        seconds = str(self.seconds)
        minutes = str(self.minutes)

        # saadaan aika päivittymään oikean näköisena kv puolelle
        # lisää "puuttuvan" nollan aikamerkintään; 00:00
        if len(seconds) < 2:
            seconds = f"0{seconds}"

        if len(minutes) < 2:
            minutes = f"0{minutes}"

        aika = f"{minutes}:{seconds}"

        # minne aikatieto tallennetaan
        if self.mika_nappi == 1:
            self.timer1 = aika
        elif self.mika_nappi == 2:
            self.timer2 = aika
        elif self.mika_nappi == 3:
            self.timer3 = aika

    def update_seconds(self):
        """sekunnin päivitys"""
        if self.general_progress < self.length:
            self.seconds += 1

            # update_minutes() kutsutaan jos sekunnit enemmän kuin 60, samalla nollataaan sekunnit
            if self.seconds == 60:
                self.update_minutes()
                self.seconds = 0

        else:
            self.seconds = 0
            self.minutes = 0

            # pysäytetään kello
            self.timer_progress.cancel()

            # asetetaan muuttuja alkutilaan, jos audio soi loppuun
            self.ids.play_one.disabled = False
            self.ids.play_two.disabled = False
            self.ids.play_three.disabled = False

    def update_minutes(self):
        """minuutin päivitysfunktio"""
        self.minutes += 1
