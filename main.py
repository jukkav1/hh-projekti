from kivy import require

# from diary import Diary
from exercise import Exercise
from skeduler import Skeduler
from kivy.properties import ListProperty
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.label import Label

# vaaditaan tietty kivy -versio
require("2.1.0")

""" kivy vaatii, että ohjelman "perusluokka" periytyy App -luokasta, joka luokka löytyy: kivy_asennushakemisto/kivy/app.py """

from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen

# jotta kv tiedosto saadaan luettua
from kivy.lang import Builder

# Boxlayout "split" ruutua varten
from kivy.uix.boxlayout import BoxLayout

# Kokoruutu vai ikkuna
# Window.fullscreen = True
Window.size = (360, 640)

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
    """PääAppi"""

    time = StringProperty()

    def disclaimer(self, dt):
        # mitenkä saadaan label ja button yhtä aikaa näkymähän? :D
        # content = Label(text="liirum\nlaarum", size_hint=(1, 1), color=(0, 0, 0, 1))
        content = Button(text="ok", size_hint=(0.1, 0.1), color=(0, 0, 0, 1))
        popup = Popup(
            title="oma vikas",
            title_color=(0, 0, 0, 1),
            content=content,
            size_hint=(0.6, 0.6),
            background="images/tausta-lehdet.png",
        )
        content.bind(on_press=popup.dismiss)
        popup.open()

    # alustetaan (konstruktoidaan) juuriolio, pääkikkare, root widget, what ever
    def build(self):
        # palautetaan kv:sta rakennettu objektiköntsä (siis koko ikkunamöhkäle)
        Clock.schedule_once(self.disclaimer, 1)
        return MainWindow()


if __name__ == "__main__":
    HH().run()
