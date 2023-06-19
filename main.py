import kivy

from diary import Diary
from exercise import Exercise
from skeduler import Skeduler
from time import time
from kivy.properties import ListProperty
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty

# vaaditaan tietty kivy -versio
kivy.require("2.1.0")


""" kivy vaatii, että ohjelman "perusluokka" periytyy App -luokasta, joka luokka löytyy: kivy_asennushakemisto/kivy/app.py """

from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
import time

# jotta kv tiedosto saadaan luettua
from kivy.lang import Builder

# Boxlayout "split" ruutua varten
from kivy.uix.boxlayout import BoxLayout

# Kokoruutu vai ikkuna
# Window.fullscreen = True
# Window.size = (280, 650)
Builder.load_file("kv/hh.kv")
# Kokoruutu vai ikkuna
# Window.fullscreen = True
# Window.size = (280, 650)
Builder.load_file("kv/hh.kv")


class MainWindow(BoxLayout):
    """pääikkuna"""


class Home(Screen):
    """Aloitusruutu"""


######
# Diary ja exercise importataan ulkopuolelta
######


# noudatetaan siis sääntöä, että "perusluokka" periytyy kivyn omasta App -luokasta.
class HH(MDApp):
    time = StringProperty()

    """PääAppi"""

    # alustetaan (konstruktoidaan) juuriolio, pääkikkare, root widget, what ever
    def build(self):
        # palautetaan kv:sta rakennettu objektiköntsä (siis koko ikkunamöhkäle)
        return MainWindow()


if __name__ == "__main__":
    HH().run()
