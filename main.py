import kivy
from diary import *

kivy.require("2.1.0")  # vaaditaan tietty kivy -versio

""" kivy vaatii, että ohjelman "perusluokka" periytyy App -luokasta, joka luokka löytyy: kivy_asennushakemisto/kivy/app.py """

# otetaan hyödyllisiä kirjastoja käyttöön
from kivymd.app import MDApp
from kivy.core.window import Window

# Välilehtiä varten
from kivy.uix.screenmanager import Screen

# jotta kv tiedosto saadaan luettua
from kivy.lang import Builder

# äänien toistoa varten
from kivy.core.audio import SoundLoader

# Boxlayout "split" ruutua varten
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

# sivun scrollaus
from kivymd.uix.scrollview import MDScrollView

# pois pääikkunasta
Window.size = (280, 650)


# tehdään luokka navigoinnille
class ContentNavigationDrawer(MDScrollView):
    # jotta tunnistetaan elementit ja voidaan viitata niihin vapaammin https://kivy.org/doc/stable/api-kivy.properties.html
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class MainWindow(BoxLayout):
    """pääikkuna"""


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


class Home(Screen):
    pass


# noudatetaan siis sääntöä, että "perusluokka" periytyy kivyn omasta App -luokasta.
class HH(MDApp):
    """PääAppi"""

    # alustetaan (konstruktoidaan) juuriolio, pääkikkare, root widget, what ever
    def build(self):
        # palautetaan kv:sta rakennettu objektiköntsä (siis koko ikkunamöhkäle)
        return MainWindow()


if __name__ == "__main__":
    HH().run()
