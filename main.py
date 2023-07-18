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
            yhteys omaan lääkäriisi avun 
            saamiseksi.""",
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

    # alustetaan (konstruktoidaan) juuriolio, pääkikkare, root widget, what ever
    def build(self):
        # palautetaan kv:sta rakennettu objektiköntsä (siis koko ikkunamöhkäle)
        Clock.schedule_once(self.disclaimer, 1)
        return MainWindow()


if __name__ == "__main__":
    HH().run()
