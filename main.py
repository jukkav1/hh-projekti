import kivy

from diary import *
from exercise import *
from skeduler import *

kivy.require("2.1.0")

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
Builder.load_file("skeduler/skeduler.kv")
Builder.load_file("skeduler/months.kv")
Builder.load_file("skeduler/dates.kv")
Builder.load_file("skeduler/select.kv")
Builder.load_file("skeduler/status.kv")
Builder.load_file("skeduler/days.kv")


class MainWindow(BoxLayout):
    """pääikkuna"""


class Home(Screen):
    """Aloitusruutu"""


######
# Diary ja exercise importataan ulkopuolelta
######


# noudatetaan siis sääntöä, että "perusluokka" periytyy kivyn omasta App -luokasta.
class HH(MDApp):

    """PääAppi"""

    # alustetaan (konstruktoidaan) juuriolio, pääkikkare, root widget, what ever
    def build(self):
        # palautetaan kv:sta rakennettu objektiköntsä (siis koko ikkunamöhkäle)
        return MainWindow()


if __name__ == "__main__":
    HH().run()
