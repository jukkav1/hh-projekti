from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen
import db.dbfunc as dbase
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput


# Container kuori sisältöä varten, tarvitaan taustakuvaa varten
class DatePickerContainer(Screen):
    pass


class DatePicker(BoxLayout):
    def merkinta_popup(self, pvmlist: list):
        """pop-uppi merkinnän tekemistä varten"""
        # rakennetaan ensin layout content-muuttujaa varten, joka muuttuja voidaan sitten
        # laittaa pop-upin sisällöksi
        layout = GridLayout(cols=1, rows=2)

        # pop-up tarkistelee onko päivässä merkintä. jos on, se näytetään ruudulle.
        onkomerkinta = DatePicker.onko_merkinta(self, pvmlist)
        if onkomerkinta:
            texti = str(DatePicker.onko_merkinta(self, pvmlist)[2])
        else:
            texti = ""

        # tekstikenttä
        textbox = TextInput(
            text=texti,
            size_hint=(0.8, 0.1),
        )
        # tallenna-painike
        tallenna_btn = Button(
            text="Tallenna",
            size_hint=(1, 0.02),
            color=(0, 0, 0, 1),
            background_color=(232 / 255, 123 / 255, 0 / 255, 0.10),
        )
        # lisätään textbox ja tallennuspainike layoutiin
        layout.add_widget(textbox)
        layout.add_widget(tallenna_btn)

        # Tehdään pop-up
        popup = Popup(
            title="Merkintä",
            title_color=(0, 0, 0, 1),
            # koska pop-upilla voi olla vain yksi sisältö, se pitää ensin tehdä layout-muuttujaan ja lisätä koko layoutin sisältö siihen
            content=layout,
            size_hint=(0.8, 0.8),
            background="images/tausta-lehdet.png",
        )

        def tallenna(self):
            """apufunktio tallennukselle, jotta saadaan muuttujat ja tekstit välitettyä tietokantaa kutsuville funktioille"""
            DatePicker.tee_merkinta(self, pvmlist, textbox.text)

        # nappulan toiminnalle funktiot
        tallenna_btn.bind(on_press=tallenna)
        tallenna_btn.bind(on_press=popup.dismiss)

        # näytetään vihdoin pop-up
        popup.open()

    def tee_merkinta(self, pvmlist: list, text: str):
        """Tekee merkintöjä päiväkirjaan. text -muuttujalla otetaan päiväkirjamerkintä"""
        self.pvmlist = pvmlist

        # onko tässä järkeä?
        pvm = pvmlist[0]
        kk = pvmlist[1]
        yy = pvmlist[2]

        # Tarkistetaan merkintä ja toimitaan sen mukaisesti
        d = DatePicker.tarkista_merkinta(self, pvmlist)
        if d:
            print(f"{pvm} {kk} {yy} on jo merkintä:", d)
        else:
            # jos ei ole merkintää, tee semmonen
            dbase.tee_merkinta(pvmlist[0], pvmlist[1], pvmlist[2], text)

    def onko_merkinta(self, pvmlist: list) -> bool:
        """Tarkistaa, onko tietokannassa merkintää tietyllä päivämäärällä ja palauttaa listan tai Falsen sen mukaan, oliko."""
        d = self.tarkista_merkinta(pvmlist)
        if d:
            print("oli merkinnät", d)
            return d[0]
        print("Ei merkintöjä")
        return False

    def tarkista_merkinta(self, pvmlist: list) -> list:
        """Palauttaa tietokannasta päiväkirjamerkinnät. jos ei ole, tyhjä lista"""
        merkintalista = dbase.hae_merkinta(pvmlist[0], pvmlist[1], pvmlist[2])
        return merkintalista

    def hae_merkintalista(kkyylist: list) -> list:
        """Hakee kaikki kuukauden merkinnät ja palauttaa ne listana"""
        merkintalista = dbase.hae_lista(kkyylist[0], kkyylist[1])
        return merkintalista


# Ladataan Kv file. Miksi pitää olla viimeisenä .. ?
Builder.load_file("kv/datepicker.kv")
