from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen
import db.dbfunc as dbase
from random import randint

# Ladataan Kv file.
Builder.load_file("kv/datepicker.kv")


# Container kuori sisältöä varten, tarvitaan taustakuvaa varten
class DatePickerContainer(Screen):
    pass


class DatePicker(BoxLayout):
    # Päivyrin pääluokka

    def tee_merkinta(
        self, pvmlist, text="DatePicker class says henlo from datepicker.py!"
    ):
        """Tekee merkintöjä päiväkirjaan. text -muuttujalla otetaan päiväkirjamerkintä, jos semmoinen tulee. Ei vielä tule :("""
        # pvmlist : [pvm, kk, yy] #pvm, kk, vuosi
        pvm = pvmlist[0]
        kk = pvmlist[1]
        yy = pvmlist[2]
        d = self.tarkista_merkinta(pvm, kk, yy)
        if d:
            print(f"{pvm} {kk} {yy} on jo merkintä:", d)
        else:
            # jos ei ole merkintää, tee semmonen
            dbase.tee_merkinta(pvm, kk, yy, text)
            print(pvm, kk, yy, text)

    def onko_merkinta(self, pvm, kk, yy) -> bool:
        """Testifunktio kysymään onko tietokannassa merkintää tietyllä päivämäärällä, ei tee vielä
        mitään järkevää"""
        print("Omko merkintäds?!")
        kakka = randint(1, 30)
        return str(kakka)

    def tarkista_merkinta(self, pvm, kk, yy) -> list:
        """Palauttaa tietokannasta päiväkirjamerkinnät. jos ei ole, tyhjä lista"""
        merkintalista = dbase.hae_merkinta(pvm, kk, yy)
        print("merkintälista:", merkintalista)
        return merkintalista
