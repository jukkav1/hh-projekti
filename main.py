from kivy import require
from exercise import Exercise
# from player import Player
from skeduler import Skeduler
from datetime import datetime
from kivy.properties import ListProperty
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

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
    """PääAppi"""

    time = StringProperty()
    date = StringProperty()

    def update(self, *args):
        self.time = str(datetime.now().strftime("%H:%M"))
        self.date = str(datetime.now().strftime("%d.%m.%Y"))

    def disclaimer(self, dt):
        layout = BoxLayout(orientation="vertical")
        label = Label(
            text="""            
            Tämä sovellus ei ole virallisesti
            hyväksytty terapiamuoto.
            Sovellusta ei ole tarkoitettu
            korvaamaan mielenterveyspalveluja.
            Jos sinulla tai läheiselläsi on
            mielenterveysongelmiin viittaavia
            oireita, ole hyvä ja ota
            yhteys omaan lääkäriisi.""",
            halign="center",
            valign="middle",
            size_hint=(0.8, 0.1),
            color=(0, 0, 0, 1),
        )
        btn = Button(text="selvä", size_hint=(1, 0.02), color=(0, 0, 0, 1))
        layout.add_widget(label)
        layout.add_widget(btn)

        popup = Popup(
            title="Huomio!",
            title_color=(0, 0, 0, 1),
            content=layout,
            size_hint=(0.8, 0.8),
            background="images/tausta-lehdet.png",
        )
        btn.bind(on_press=popup.dismiss)
        popup.open()

    def build(self, *args):
        Clock.schedule_interval(self.update, 1)
        Clock.schedule_once(self.disclaimer, 1)
        return MainWindow()


if __name__ == "__main__":
    HH().run()
