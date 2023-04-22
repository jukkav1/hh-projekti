import kivy

kivy.require("2.1.0")  # vaaditaan tietty kivy -versio

""" kivy vaatii, että ohjelman "perusluokka" periytyy App -luokasta, joka luokka löytyy: kivy_asennushakemisto/kivy/app.py """

# otetaan hyödyllisiä luokkia käyttöön
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button


class MainWindow(GridLayout):
    """GridLayout -tyyppinen pääikkuna (luokka)"""

    def callback(self, kv):
        """painikkeen tapahtumat"""
        self.label1.text = "Painoit %s" % kv.text

    def __init__(self, **kwargs):
        """ikkunan päätaso"""
        # superia kutsutaan, jotta perusluokan (LoginScreen vai GridLayout?) toiminnot eivät ylikirjoitu kokonaan, me vaan tehdään oma init -konstruktori [lähde: kivy.org/doc/stable/guide/basic.html]
        super(MainWindow, self).__init__(**kwargs)

        # päätasolla on vain yksi "sarake"
        self.cols = 1

        # tila ohjelman "näkymälle", lammas tähän?
        self.label1 = Label(text="Tervetuloa", color="#0000BB")
        self.add_widget(self.label1)

        # Tehdään uusi 3-sarakkeinen GridLayout päätason sisään
        self.bottomgrid = GridLayout()
        self.bottomgrid.cols = 3

        self.nappula1 = Button(text="Merkinnät", background_color="#AAAA00")
        self.nappula1.bind(on_release=self.callback)
        self.bottomgrid.add_widget(self.nappula1)

        self.nappula2 = Button(text="Alkuun")
        self.nappula2.bind(on_release=self.callback)
        self.bottomgrid.add_widget(self.nappula2)

        self.nappula3 = Button(text="Harjoitteet", background_color="#00AA00")
        self.nappula3.bind(on_release=self.callback)
        self.bottomgrid.add_widget(self.nappula3)

        # Quit -nappula toimii jo. Quit on punainen
        self.nappula4 = Button(text="Quit", background_color="#FF2020")
        self.nappula4.bind(on_release=exit)
        self.add_widget(self.nappula4)

        self.add_widget(self.bottomgrid)


class MainBackground(Widget):
    def __init__(self, **kwargs):
        super(MainBackground, self).__init__(**kwargs)
        pass


# noudatetaan siis sääntöä, että "perusluokka" periytyy kivyn omasta App -luokasta.
class HH(App):
    # alustetaan (konstruktoidaan) juuriolio, pääkikkare, root widget, what ever
    def build(self):
        # palautetaan MainWindow
        return MainWindow()


if __name__ == "__main__":
    HH().run()
