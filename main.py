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
    def callback(self, kv):
        self.label1.text = "Painoit %s" % kv.text

    def __init__(self, **kwargs):
        """superia kutsutaan, jotta perusluokan (LoginScreen vai GridLayout?) toiminnot eivät ylikirjoitu kokonaan, me vaan tehdään oma init -konstruktori [lähde: kivy.org/doc/stable/guide/basic.html]"""
        super(MainWindow, self).__init__(**kwargs)
        self.rows = 2
        self.cols = 3

        self.label1 = Label(text="Velkam", color="#0000BB")
        self.add_widget(self.label1)

        self.nappula1 = Button(text="Merkinnät", background_color="#AAAA00")
        self.nappula1.bind(on_release=self.callback)
        self.add_widget(self.nappula1)

        self.nappula2 = Button(text="Alkuun")
        self.nappula2.bind(on_release=self.callback)
        self.add_widget(self.nappula2)

        self.nappula3 = Button(text="Harjoitteet", background_color="#00AA00")
        self.nappula3.bind(on_release=self.callback)
        self.add_widget(self.nappula3)

        # Quit -nappula toimii jo. Quit on punainen
        self.nappula4 = Button(text="Quit", background_color="#FF2020")
        self.nappula4.bind(on_release=exit)
        self.add_widget(self.nappula4)

class MainBackground(Widget):
    def __init__(self, **kwargs):
        super(MainBackground, self).__init__(**kwargs)
        pass


# noudatetaan siis sääntöä, että "perusluokka" periytyy kivyn omasta App -luokasta.
class HH(App):
    # alustetaan (konstruktoidaan) juuriolio, pääkikkare, root widget, what ever
    def build(self):
        # palautetaan ainoastaan Label -nimike, jonka tekstinä .. "hello world".
        return MainWindow()


if __name__ == "__main__":
    HH().run()
