# Copyright (c) 2023 Taru Haapala
# Copyright (c) 2023 Jukka Valvanne

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen
import db.dbfunc as dbase
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from datetime import datetime
from kivy.properties import StringProperty
from kivy.properties import NumericProperty


# Container kuori sisältöä varten, tarvitaan taustakuvaa varten
class DatePickerContainer(Screen):
    date = StringProperty(str(datetime.now().strftime("%d.%m.%Y")))

    def update(self, *args):  # update kutsutaan kellon päivityksen yhteydessä
        """Ajan ja päiväyksen muunto oikeaan suomalaiseen muotoon:
        %H = tunnit 24h, %M: minuutti, %d: päivä, %m: kuukausi nro, %Y: Vuosi neljällä merkillä ( %y kahdella )
        """
        # .strftime = muotoile aika/pvm haluttuun muotoon
        self.time = str(datetime.now().strftime("%H:%M"))


class DatePicker(BoxLayout):
    year = NumericProperty(datetime.now().year)
    month = NumericProperty(datetime.now().month)

    def merkinta_popup(self, datelist: list):
        """pop-uppi merkinnän tekemistä varten"""
        # rakennetaan ensin layout content-muuttujaa varten, joka muuttuja voidaan sitten
        # laittaa pop-upin sisällöksi
        layout = GridLayout(cols=1, rows=2)

        # Tarkista onko päivässä merkintä. jos on, teksti (vastauksessa indeksi 2) näytetään ruudulle.
        # Parametrin välitystä voi siistiä. Tunnustan.
        if self.onko_merkinta(datelist):
            text_str = str(self.onko_merkinta(datelist)[3])
        else:
            text_str = ""

        # tekstikenttä
        textbox = TextInput(
            text=text_str,
            size_hint=(0.8, 0.1),
        )
        # tallenna-painike
        save_btn = Button(
            text="Tallenna",
            size_hint=(1, 0.02),
            color=(0, 0, 0, 1),
            background_color=(232 / 255, 123 / 255, 0 / 255, 0.10),
        )
        # lisätään textbox ja tallennuspainike layoutiin
        layout.add_widget(textbox)
        layout.add_widget(save_btn)

        # Tehdään pop-up
        popup = Popup(
            title="Merkintä",
            title_color=(0, 0, 0, 1),
            # koska pop-upilla voi olla vain yksi sisältö, se pitää ensin tehdä layout-muuttujaan ja lisätä koko layoutin sisältö siihen
            content=layout,
            size_hint=(0.8, 0.8),
            background="images/tausta-lehdet.png",
        )

        def save_helper(self):
            """apufunktio tallennukselle, jotta saadaan muuttujat ja tekstit välitettyä tietokantaa kutsuville funktioille"""
            DatePicker.tee_merkinta(self, datelist, textbox.text)

        # nappulan toiminnalle funktiot
        save_btn.bind(on_press=save_helper)
        save_btn.bind(on_press=popup.dismiss)

        # näytetään vihdoin pop-up
        popup.open()

    def tee_merkinta(self, datelist: list, text: str):
        """Tekee merkintöjä päiväkirjaan. text -muuttujalla otetaan päiväkirjamerkintä"""

        # onko tässä järkeä?
        day = datelist[0]
        month = datelist[1]
        year = datelist[2]

        # Tarkistetaan merkintä ja toimitaan sen mukaisesti
        is_entry_days_list = DatePicker.check_single_day(self, datelist)
        if is_entry_days_list:
            print(f"{day} {month} {year} on jo merkintä:", is_entry_days_list)
        else:
            # jos ei ole merkintää, tee semmonen
            dbase.create_entry(day, month, year, text)

    ##### Tässä saattaa olla kaksi samankaltaista funktiota toiminnolle, jonka voi ehkä tehdä yhdelläkin.
    def onko_merkinta(self, datelist: list) -> bool:
        """Tarkistaa, onko tietokannassa merkintää tietyllä päivämäärällä ja palauttaa listan tai Falsen sen mukaan, oliko."""
        day_entry = self.check_single_day(datelist)
        if day_entry:
            print("oli merkintä", day_entry)
            return day_entry[0]
        print("Ei merkintöjä")
        return False

    def check_single_day(self, datelist: list) -> list:
        """Palauttaa tietokannasta päiväkirjamerkinnät. jos ei ole, tyhjä lista"""
        day = datelist[0]
        month = datelist[1]
        year = datelist[2]

        entrylist = dbase.get_single_entry(day, month, year)
        return entrylist

    #########

    def get_month_entrylist(month_year: list) -> list:
        """Hakee kaikki kuukauden merkinnät ja palauttaa ne listana"""
        month = month_year[0]
        year = month_year[1]
        entrylist = dbase.get_entry_list(month, year)
        return entrylist


# Ladataan Kv file. Miksi pitää olla viimeisenä .. ?
Builder.load_file("kv/datepicker.kv")
