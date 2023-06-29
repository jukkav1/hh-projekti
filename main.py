from kivy import require
from exercise import Exercise
from skeduler import Skeduler
from time import asctime
from kivy.properties import ListProperty
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock

# vaaditaan tietty kivy -versio
require("2.1.0")

# Kokoruutu vai ikkuna
# Window.fullscreen = True
Window.size = (360, 640)

Builder.load_file("kv/hh.kv")


class MainWindow(BoxLayout):
    """pääikkuna"""


class Home(Screen):
    """Aloitusruutu"""


# noudatetaan siis sääntöä, että "perusluokka" periytyy kivyn omasta App -luokasta.
class HH(MDApp):
    time = StringProperty()

    def update(self, *args):
        self.time = str(asctime())

    def build(self, *args):
        Clock.schedule_interval(self.update, 1)
        return MainWindow()


if __name__ == "__main__":
    HH().run()
