from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.core.audio import SoundLoader
from kivy.properties import NumericProperty, StringProperty
from kivy.clock import Clock

Builder.load_file("kv/exercise.kv")


class Exercise(Screen):
    # määritetään mitä muuttuja on (string tai numeric)
    length = NumericProperty(0.0)
    progress = NumericProperty(0.0)
    # tähän tuodaan lopullinen aikatieto, joka voidaan näyttää MDLabelissa, aluksi aika on "00:00"
    timer = StringProperty("00:00")
    seconds = NumericProperty()
    minutes = NumericProperty()
    audio_playing = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sound = SoundLoader.load("sounds/test.ogg")
        # self.sound = SoundLoader.load("sounds/mixkit-evil-storm-atmosphere-2404.wav")

    # vaatii vielä kikkailua jos audio soi loppuun ilman että pausettaa
    def play_stop_audio(self):
        # jos audio löytyy:
        if self.sound:
            # jos audio on päällä ja se halutaan pysäyttää
            # aktivoituu kun nappia painetaan vain yksi nappi(play/pause kerrallaan aktiivinen riippuen audio_playing tilasta)
            if self.audio_playing == True:
                # voidaan lopettaa audio, jos se on käynnissä
                self.sound.stop()
                self.audio_playing = False
                # asetetaan muuttujat takaisin alkutilaan jos audio pysäytetään
                self.timer = "00:00"
                self.progress = 0
                self.seconds = 0
                self.minutes = 0
                # lopetetaan Clock.schedule_interval:n toiminta progsessipalkissa ja ajassa
                self.bar_progress.cancel()
                self.timer_progress.cancel()
                print(f"äänet kuoli. self.audio_playing={self.audio_playing}")
                # muutetaan kuvake takasin "play"-kuvakkeeksi
                self.update_icon()
            # ensin mennään tänne ja käynnistetään audio
            elif self.audio_playing == False:
                # jos audio ei käynnistä, käynnistetään
                self.sound.play()
                self.audio_playing = True
                # asetetaan audio pituus length muuttujaan
                self.length = self.sound.length
                # clock_shedule_interval määrittää miten usein progressipalkki(update_progres_bar) päivitetään,tässä sekunnin välein (1.0)
                # tämä käynnissä kunnes sen toimita lopetetaan (.cancel())
                # tehdään samalla bar_progress(muuttuja jolla voi myöhemmin lopettaa  Clokin toiminnan)
                self.bar_progress = Clock.schedule_interval(
                    self.update_progress_bar, 1.0
                )
                # clock_shedule_interval määrittää miten usein  päivitetään string_time päivitetään. tässä sekunnin välein (1.0)
                # tehdään samalla timer_progress(muuttuja jolla voi myöhemmin lopettaa  Clokin toiminnan)
                self.timer_progress = Clock.schedule_interval(self.string_time, 1.0)
                # muutetaan kuvake "pause" kuvakkeeksi
                self.update_icon()
                print(f"kuuluu ääniä! self.audio_playing={self.audio_playing}")
        # jos ääntä ei löydy
        else:
            print("äänen toisto ei onnistu T_T")

    def update_icon(self):
        # katsotaan mikä kuvake käytössä ja muutetaan se toiseksi
        #  etsii iconbuttonin nimeltä "play_stop_btn" ja vaihtaa siihen oikean kuvakkeen tilanteen mukaan
        if self.ids.play_stop_btn1.icon == "play":
            self.ids.play_stop_btn1.icon = "pause"
        else:
            self.ids.play_stop_btn1.icon = "play"

    # mitä tehdään progressipalkille kun audio käynnissä (Clock.schedule_interval(self.update_progress_bar, 1.0)) tulee tänne
    def update_progress_bar(self, dt):  # ei toimi ilman kahta dt=datetime?
        # palkkiä päivitetään niin kauan kun audio soi
        if self.progress < self.length:
            self.progress += 1
        # kun audio loppuu:
        else:
            self.progress = 0  # nollataan progressipalkki
            self.bar_progress.cancel()  # lopetataan progressipalkin päivittäminen(Clock.schedule_interval(self.update_progress_bar, 1.0))

    # kerrotaan Clock.schedule_interval(self.string_time, 1.0) ohjeet miten toimia
    def string_time(self, dt):
        # aletaan päivittää sekuntteja
        self.update_seconds()
        seconds = str(self.seconds)
        minutes = str(self.minutes)

        # määritetään näin jotta timer näyttää sekunnit oikein, jos <2 arvoa muuttaa, edessä oleva nolla joko häviää tai jää kummittelemaan
        # jos aika nousee yli 10 sekunnin (aka en osaa selittää kunnolla kokeile itse niin tajuat paremmin :P)
        if len(seconds) < 2:
            seconds = f"0{seconds}"
        # jos aika sekunnit menee yli 60, otetaan minuutit käyttöön
        if len(minutes) < 2:
            minutes = f"0{minutes}"

        # siirretään aika timeriin ja siitä MDLabeliin näkyviin
        self.timer = f"{minutes}:{seconds}"

    # kerrotaan miten sekunnit päivitetään
    def update_seconds(self):
        # jos audio käynnissä
        if self.progress < self.length:
            self.seconds += 1

            if self.seconds == 60:
                self.update_minutes()
                self.seconds = 0
        # jos audio ei ole käynnissä
        else:
            self.seconds = 0
            self.minutes = 0
            self.timer_progress.cancel()

    # päivitetään minuutit aikaa varten, jos sekunnit 60
    def update_minutes(self):
        self.minutes += 1
