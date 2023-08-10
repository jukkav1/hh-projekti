from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen
import db.dbfunc as dbase
from random import randint
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.properties import NumericProperty, StringProperty


# Container kuori sisältöä varten, tarvitaan taustakuvaa varten
class DatePickerContainer(Screen):
    pass


class DatePicker(BoxLayout):
    def kakkaa(eka, toka):
        print(eka, toka)
        pass

    def merkinta_popup(self, pvmlist):
        print(pvmlist)
        """vastuunvapautuslause pop-uppi"""
        # rakennetaan ensin layout content-muuttujaa varten, joka muuttuja voidaan sitten
        # laittaa pop-upin sisällöksi
        layout = GridLayout(cols=1, rows=2)

        # pop-up tarkistelee onko päivässä merkintä. jos on, se näytetään ruudulle.
        # Jos ei ole, sanotaan, ettei ole.
        onkomerkinta = DatePicker.onko_merkinta(self, pvmlist)
        if onkomerkinta:
            texti = str(DatePicker.onko_merkinta(self, pvmlist)[2])
        else:
            texti = "Merkintää ei ole"

        textbox = TextInput(
            text=texti,
            size_hint=(0.8, 0.1),
        )
        tallenna_btn = Button(
            text="Tallenna",
            size_hint=(1, 0.02),
            color=(0, 0, 0, 1),
            background_color=(232 / 255, 123 / 255, 0 / 255, 0.10),
        )
        layout.add_widget(textbox)
        layout.add_widget(tallenna_btn)

        popup = Popup(
            title="Merkintä",
            title_color=(0, 0, 0, 1),
            content=layout,
            size_hint=(0.8, 0.8),
            background="images/tausta-lehdet.png",
        )
        # nappulan toiminnalle funktio
        tallenna_btn.bind(on_press=popup.dismiss)

        # näytetään vihdoin pop-up
        popup.open()

    # Päivyrin pääluokka

    def tee_merkinta(
        self, pvmlist, text="DatePicker class says henlo from datepicker.py!"
    ):
        """Tekee merkintöjä päiväkirjaan. text -muuttujalla otetaan päiväkirjamerkintä, jos semmoinen tulee. Ei vielä tule :("""
        # pvmlist : [pvmlist] #pvm, kk, vuosi
        pvm = pvmlist[0]
        kk = pvmlist[1]
        yy = pvmlist[2]
        d = self.tarkista_merkinta(pvmlist)
        if d:
            print(f"{pvm} {kk} {yy} on jo merkintä:", d)
        else:
            # jos ei ole merkintää, tee semmonen
            dbase.tee_merkinta(pvmlist[0], pvmlist[1], pvmlist[2], text)
            print(pvmlist, text)

    def onko_merkinta(self, pvmlist) -> bool:
        """Testifunktio kysymään onko tietokannassa merkintää tietyllä päivämäärällä, ei tee vielä
        mitään järkevää"""
        d = self.tarkista_merkinta(pvmlist)
        if d:
            print("oli merkinnät", d)
            return d[0]
        print("Ei oleeee")
        return False

    def tarkista_merkinta(self, pvmlist) -> list:
        """Palauttaa tietokannasta päiväkirjamerkinnät. jos ei ole, tyhjä lista"""
        merkintalista = dbase.hae_merkinta(pvmlist[0], pvmlist[1], pvmlist[2])
        # print("merkintälista:", merkintalista)
        return merkintalista

    def hae_merkintalista(kkyylist) -> list:
        oma_kk = kkyylist[0]
        oma_yy = kkyylist[1]
        merkintalista = dbase.hae_lista(oma_kk, oma_yy)
        print(merkintalista)
        return merkintalista
        # return ["10", "20", "30"]


# Ladataan Kv file.
Builder.load_file("kv/datepicker.kv")
