from kivy import require
from exercise import Exercise
from datetime import datetime
from kivy.properties import StringProperty
from kivy.properties import NumericProperty
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from datepicker import DatePicker

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


class HH(MDApp):
    """PääAppi"""

    # Kalenterille hyödyllisiä muuttujia
    time = StringProperty()
    date = StringProperty()
    month = NumericProperty(datetime.now().month)
    year = NumericProperty(datetime.now().year)

    def update(self, *args):
        """Ajan ja päiväyksen muunto oikeaan suomalaiseen muotoon"""
        self.time = str(datetime.now().strftime("%H:%M"))
        self.date = str(datetime.now().strftime("%d.%m.%Y"))

    def disclaimer(self, dt):
        """vastuunvapautuslause pop-uppi"""
        # rakennetaan ensin layout content-muuttujaa varten, joka muuttuja voidaan sitten laittaa pop-upin sisällöksi
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
        btn = Button(
            text="selvä",
            size_hint=(1, 0.02),
            color=(0, 0, 0, 1),
            background_color=(232 / 255, 123 / 255, 0 / 255, 0.10),
        )
        layout.add_widget(label)
        layout.add_widget(btn)

        popup = Popup(
            title="Huomio!",
            title_color=(0, 0, 0, 1),
            content=layout,
            size_hint=(0.8, 0.8),
            background="images/tausta-lehdet.png",
        )
        # nappulan toiminnalle funktio
        btn.bind(on_press=popup.dismiss)
        # näytetään vihdoin pop-up
        popup.open()

    def build(self, *args):
        # päivämäärän päivitys käyntiin, mikä ja montako sekuntia
        Clock.schedule_interval(self.update, 1)
        # disclaimerin triggeri
        Clock.schedule_once(self.disclaimer, 1)
        return MainWindow()


if __name__ == "__main__":
    HH().run()
