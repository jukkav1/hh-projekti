import kivy

kivy.require("2.1.0")  # vaaditaan tietty kivy -versio

""" kivy vaatii, että ohjelman "perusluokka" periytyy App -luokasta, joka luokka löytyy: kivy_asennushakemisto/kivy/app.py """

# otetaan hyödyllisiä kirjastoja käyttöön
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import (
    ScreenManager,
    Screen,
)  # tämä tuodaan välilehtiä varte
from kivy.lang import Builder  # tämä tuodaan, jotta kv tiedosto saadaan luettua


class MainWindow(Screen):  # aikasemmin GridLayout:
    pass


#    """GridLayout -tyyppinen pääikkuna (luokka)"""
#
#    Window.size = (280, 650)  # Onko hyvä määritellä tässä vai jossain muualla?
#
#    def callback(self, kv):
#        """painikkeen tapahtumat"""
#        self.label1.text = "Painoit %s" % kv.text
#
#    def __init__(self, **kwargs):
#        """ikkunan päätaso"""
#        # superia kutsutaan, jotta perusluokan (LoginScreen vai GridLayout?) toiminnot eivät ylikirjoitu kokonaan, me vaan tehdään oma init -konstruktori [lähde: kivy.org/doc/stable/guide/basic.html]
#        self.size_hint
#        self.width = 30
#        self.height = 160
#        super(MainWindow, self).__init__(**kwargs)
#
#        # päätasolla on vain yksi "sarake"
#        self.cols = 1
#
#        # tila ohjelman "näkymälle", lammas tähän?
#        self.label1 = Label(text="Tervetuloa", color="#0099BB", font_size=40)
#        self.add_widget(self.label1)
#
#        # Tehdään uusi 3-sarakkeinen GridLayout päätason sisään
#        self.bottom_grid = GridLayout()
#        self.bottom_grid.size_hint_y = None
#        self.bottom_grid.height = 90
#        self.bottom_grid.cols = 3
#
#        # layoutin rakennuslogiikkaa, järjestystä etc on syytä parantaa erim. for-loopilla tms.
#        self.nappula1 = Button(text="Merkinnät", background_color="#AAAA00")
#        self.nappula1.bind(on_release=self.callback)
#        self.bottom_grid.add_widget(self.nappula1)
#
#        self.nappula2 = Button(text="Alkuun")
#        self.nappula2.bind(on_release=self.callback)
#        self.bottom_grid.add_widget(self.nappula2)
#
#        self.nappula3 = Button(text="Harjoitteet", background_color="#00AA00")
#        self.nappula3.bind(on_release=self.callback)
#        self.bottom_grid.add_widget(self.nappula3)
#
#        # # Quit -nappula toimii jo. Quit on punainen
#        # self.nappula4 = Button(text="X", background_color="#FF2020", font_size=80)
#        # self.nappula4.bind(on_release=exit)
#        # self.add_widget(self.nappula4)
#
#        # lopuksi liimataan itse bottomgrid -widget pääikkunan gridiin
#        self.add_widget(self.bottom_grid)


class Diary(Screen):
    pass


class Exercise(Screen):
    pass


class WindowManager(ScreenManager):  # ikkunoiden  määrittämistä varten
    pass


kv = Builder.load_file("hh.kv")  # ladataan kv tiedosto


# noudatetaan siis sääntöä, että "perusluokka" periytyy kivyn omasta App -luokasta.
class HH(App):
    # alustetaan (konstruktoidaan) juuriolio, pääkikkare, root widget, what ever
    def build(self):
        # palautetaan MainWindow
        return kv  # aikaisemmin return MainWindow()


if __name__ == "__main__":
    HH().run()
