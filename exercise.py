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
    bar_progress1 = NumericProperty(0.0)
    bar_progress2 = NumericProperty(0.0)
    bar_progress3 = NumericProperty(0.0)
    timer1 = StringProperty("00:00")
    timer2 = StringProperty("00:00")
    timer3 = StringProperty("00:00")
    seconds = NumericProperty()
    minutes = NumericProperty()
    mika_nappi = 0
    audio_playing = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # miten saadaan karsittua yhdeksi napiksi, niin että saadaan aina oikea audio päälle, pois?
    def Button1(self, soundfile):
        # ladataan äänitiedosto
        self.sound = SoundLoader.load(soundfile)
        self.mika_nappi = 1

        if self.sound:
            if self.audio_playing == False:
                self.audio_playing = True
                print("äänet löytyy")
                self.sound.play()
                self.audio_playing = True
                #otetaan play napit pois käytöstä toistaiseksi
                self.ids.play_one.disabled=True
                self.ids.play_two.disabled=True
                self.ids.play_three.disabled=True
                self.length = self.sound.length
                # käynnistetään kello jotta latauspalkki ja ajasti lähtee pyörimään, määritetään kuinka usein päivitetään(tässä sekunnin välein)
                self.bar_progress = Clock.schedule_interval(
                    self.update_progress_bar, 1.0
                )
                self.timer_progress = Clock.schedule_interval(self.string_time, 1.0)
        else:
            print("ei ole ääntä")

    def Button2(self, soundfile):
        self.sound = SoundLoader.load(soundfile)
        self.mika_nappi = 2

        if self.sound:
            print("äänet löytyy")
            # käynnistetää audio
            self.sound.play()
            self.audio_playing = True
            self.ids.play_one.disabled=True
            self.ids.play_two.disabled=True
            self.ids.play_three.disabled=True
            # määritetään myöhempää käyttöä varten
            self.length = self.sound.length
            self.bar_progress = Clock.schedule_interval(self.update_progress_bar, 1.0)
            self.timer_progress = Clock.schedule_interval(self.string_time, 1.0)
    
    def Button3(self, soundfile):
        self.sound = SoundLoader.load(soundfile)
        self.mika_nappi = 3

        if self.sound:
            print("äänet löytyy")
            # käynnistetää audio
            self.sound.play()
            self.audio_playing = True
            self.ids.play_one.disabled=True
            self.ids.play_two.disabled=True
            self.ids.play_three.disabled=True
            # määritetään myöhempää käyttöä varten
            self.length = self.sound.length
            self.bar_progress = Clock.schedule_interval(self.update_progress_bar, 1.0)
            self.timer_progress = Clock.schedule_interval(self.string_time, 1.0)

    # pysäytetään audio stop napista
    def stop_audio(self):
        if self.audio_playing == True:
            self.audio_playing = False
            #play napit takaisin käyttöön
            self.ids.play_one.disabled=False
            self.ids.play_two.disabled=False
            self.ids.play_three.disabled=False
            self.clear_time()
            # pysäytetään audio
            self.sound.stop()
            print("ääni seisautettu")

    # nollataan muuttuja takaisin alkutilaan, pysäytetään kello, jos stop nappia painetaan
    def clear_time(self):
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

    # miten lautaspalkkia päivitetään
    def update_progress_bar(self, dt):
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

    # miten aikaa päivitetään
    def string_time(self, dt):
        self.update_seconds()
        # aika muutetaan sellaiseksi minkä kv puolen label ymmärtää
        seconds = str(self.seconds)
        minutes = str(self.minutes)

        # saadaan aika päivittymään oikean näköisena kv puolelle
        if len(seconds) < 2:
            seconds = f"0{seconds}"

        if len(minutes) < 2:
            minutes = f"0{minutes}"

        aika = f"{minutes}:{seconds}"
        # minne tieto tallennetaan

        if self.mika_nappi == 1:
            self.timer1 = aika
        elif self.mika_nappi == 2:
            self.timer2 = aika
        elif self.mika_nappi == 3:
            self.timer3 = aika

    # miten sekunnit päivitetään
    def update_seconds(self):
        if self.general_progress < self.length:
            self.seconds += 1

            if self.seconds == 60:
                # update minutes kutsutaan jos sekunnit enemmän kuin 60, samalla nollataaan sekunnit
                self.update_minutes()
                self.seconds = 0
        else:
            self.seconds = 0
            self.minutes = 0
            # pysäytetään kello
            self.timer_progress.cancel()
            # asetetaan muuttuja alkutilaan, jos audio soi loppuun
            self.audio_playing = False
            self.ids.play_one.disabled=False
            self.ids.play_two.disabled=False
            self.ids.play_three.disabled=False

    # miten minuutit päivitetään
    def update_minutes(self):
        self.minutes += 1
