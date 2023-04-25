import kivy

kivy.require("2.1.0")  # vaaditaan tietty kivy -versio

""" kivy vaatii, että ohjelman "perusluokka" periytyy App -luokasta, joka luokka löytyy: kivy_asennushakemisto/kivy/app.py """

# otetaan hyödyllisiä kirjastoja käyttöön
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import (
    ScreenManager,
    Screen,
)  # tämä tuodaan välilehtiä varte
from kivy.lang import Builder  # tämä tuodaan, jotta kv tiedosto saadaan luettua

# vanha grid -tyylinen layout; error:
# ScreenManager accepts only Screen widget.
# from layoutgrid import *


class MainWindow(Screen):
    Window.size = (280, 650)  # Onko hyvä määritellä tässä vai jossain muualla?
    pass


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
