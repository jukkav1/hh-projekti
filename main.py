import kivy

kivy.require("2.1.0")  # vaaditaan tietty kivy -versio

""" kivy vaatii, että ohjelman "perusluokka" periytyy App -luokasta, joka luokka löytyy: kivy_asennushakemisto/kivy/app.py """

# otetaan hyödyllisiä luokkia käyttöön
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.textinput import TextInput


class LoginScreen(GridLayout):
    def callback(self, nappi):
        print("%s sanoo ouch!" % nappi.text)

    def __init__(self, **kwargs):
        """superia kutsutaan, jotta perusluokan (LoginScreen vai GridLayout?) toiminnot eivät ylikirjoitu kokonaan, me vaan tehdään oma init -konstruktori [lähde: kivy.org/doc/stable/guide/basic.html]"""
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="Nimi"))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text="salakala"))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)

        self.nappula1 = Button(text="click heres")
        self.nappula1.bind(on_release=self.callback)
        self.add_widget(self.nappula1)

        self.nappula2 = Button(text="click heres")
        self.nappula2.bind(on_release=self.callback)
        self.add_widget(self.nappula2)

        self.nappula3 = Button(text="click heres")
        self.nappula3.bind(on_release=self.callback)
        self.add_widget(self.nappula3)


# noudatetaan siis sääntöä, että "perusluokka" periytyy kivyn omasta App -luokasta.
class EkaOhjelma(App):
    # alustetaan (konstruktoidaan) juuriolio, pääkikkare, root widget, what ever
    def build(self):
        # palautetaan ainoastaan Label -nimike, jonka tekstinä .. "hello world".
        return LoginScreen()


if __name__ == "__main__":
    EkaOhjelma().run()
