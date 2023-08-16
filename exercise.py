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
    pressed_button = 0
    # toimii myös ilman näitä, laitammeko roskiin? onko jotain hyötyä näistä tässä?
    # def __init__(self, **kwargs):
    # super().__init__(**kwargs)

    # aloitetaan audio ja asetetaan arvo pressed_button muuttujalle
    def play_audio(self, soundfile: str):
        """kivyn puolen napit kutsuu tätä"""
        # ladataan äänitiedosto
        self.sound = SoundLoader.load(soundfile)
        if soundfile == "sounds/ambient_forest_new.mp3":
            self.pressed_button = 1
            # print(f"mikä nappi on {self.pressed_button}")

        elif soundfile == "sounds/lehdet.mp3":
            self.pressed_button = 2
            # print(f"mikä nappi on {self.pressed_button}")

        elif soundfile == "sounds/sade.mp3":
            self.pressed_button = 3
            # print(f"mikä nappi on {self.pressed_button}")

        # Jos ääni löytyy ..
        if self.sound:
            print("äänet löytyy")
            self.sound.play()

            # otetaan play napit pois käytöstä jos jokin ääni ON JO KÄYNNISSÄ
            self.ids.play_one.disabled = True
            self.ids.play_two.disabled = True
            self.ids.play_three.disabled = True

            # asetetaan arvo muuttujalle
            self.length = self.sound.length

            # käynnistetään kello jotta latauspalkki ja ajasti lähtee pyörimään, määritetään kuinka usein päivitetään(tässä sekunnin välein)
            self.bar_progress = Clock.schedule_interval(self.update_progress_bar, 1.0)
            self.timer_progress = Clock.schedule_interval(self.string_time, 1.0)
        else:
            print("ei ole ääntä")

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
        if self.pressed_button == 1:
            self.bar_progress1 = self.general_progress

        elif self.pressed_button == 2:
            self.bar_progress2 = self.general_progress

        elif self.pressed_button == 3:
            self.bar_progress3 = self.general_progress

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
