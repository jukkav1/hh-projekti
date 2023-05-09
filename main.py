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

# Boxlayout "split" ruutua varten
from kivy.uix.boxlayout import BoxLayout


class MainWindow(BoxLayout):
    """pääikkuna"""

    #    Builder.load_file("hh.kv")

    # Onko hyvä määritellä tässä vai jossain muualla?
    Window.size = (280, 650)


class Exercise(Screen):
    """harjoitukset"""

    def play_sound(self):
        """Äänen toistofunktio"""
        sound = SoundLoader.load("sounds/test.ogg")
        if sound:
            sound.play()
        else:
            print("äänen toisto ei onnistu T_T")
        pass


# noudatetaan siis sääntöä, että "perusluokka" periytyy kivyn omasta App -luokasta.
class HH(App):
    """PääAppi"""

    # alustetaan (konstruktoidaan) juuriolio, pääkikkare, root widget, what ever
    def build(self):
        # palautetaan kv:sta rakennettu objektiköntsä (siis koko ikkunamöhkäle)
        return MainWindow()


if __name__ == "__main__":
    HH().run()
