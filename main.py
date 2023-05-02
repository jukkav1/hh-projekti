import kivy
from diary import *

kivy.require("2.1.0")  # vaaditaan tietty kivy -versio

""" kivy vaatii, että ohjelman "perusluokka" periytyy App -luokasta, joka luokka löytyy: kivy_asennushakemisto/kivy/app.py """

# otetaan hyödyllisiä kirjastoja käyttöön
from kivy.app import App
from kivy.core.window import Window

# Välilehtiä varten
from kivy.uix.screenmanager import ScreenManager, Screen

# jotta kv tiedosto saadaan luettua
from kivy.lang import Builder

# äänien toistoa varten
from kivy.core.audio import SoundLoader


class MainWindow(Screen):
    """pääikkuna"""

    # Onko hyvä määritellä tässä vai jossain muualla?
    Window.size = (280, 650)


class Exercise(Screen):
    """harjoitukset"""


class WindowManager(ScreenManager):
    """ikkunoiden määrittämistä varten"""

    # Tämä soittaa äänen kutsuttaessa; kts. hh.kv
    def play_sound(self):
        """Äänen toistofunktio"""
        sound = SoundLoader.load("sounds/test.ogg")
        if sound:
            sound.play()
        else:
            print("äänen toisto ei onnistu T_T")


# rakennetaan objekti tiedoston perusteella
kv = Builder.load_file("hh.kv")


# noudatetaan siis sääntöä, että "perusluokka" periytyy kivyn omasta App -luokasta.
class HH(App):
    """PääAppi"""

    # alustetaan (konstruktoidaan) juuriolio, pääkikkare, root widget, what ever
    def build(self):
        # palautetaan kv:sta rakennettu objektiköntsä (siis koko ikkunamöhkäle)
        return kv


if __name__ == "__main__":
    HH().run()
