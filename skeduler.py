# Copyrighted under the MIT license, See LICENSE.
# Copyright (c) 2023 Jukka Valvanne & Taru Haapala
# Copyright (c) 2015 Kuldeep Singh

# import statements
import calendar

from datetime import datetime
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy import require as kivyreq

import db.dbfunc as db

# from random import randint

kivyreq("2.2.0")

# loaderit kivy-fileille
Builder.load_file("skeduler/months.kv")  # kuukaudet
Builder.load_file("skeduler/dates.kv")  # päivämäärät
Builder.load_file("skeduler/status.kv")  # tila-aika-jatkumo
Builder.load_file("skeduler/daylabels.kv")  # viikonpäivät

date_layout = None


class Status(BoxLayout):
    """Status -palkin luokka"""

    def __init__(self, **kwargs):
        super(Status, self).__init__(**kwargs)


class Months(BoxLayout):
    """Kuukausilistan luokka"""

    def __init__(self, **kwargs):
        super(Months, self).__init__(**kwargs)
        self.layout = None

    def valitse_kuukausi(self, mo):
        print("Jou Valitsit kuukauden ", mo)
        Skeduler.set_month(Skeduler, mo)
        layout = Skeduler.draw_month(Skeduler.year, Skeduler.month)
        Dates.push_widget(layout)


class Reminder(BoxLayout):
    """Luokka merkinnän tekoa varten; tekstikenttä ja tallennusnappula"""

    def __init__(self, **kwargs):
        super(Reminder, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.textbox = TextInput()
        self.boxlayout = BoxLayout(orientation="horizontal", size_hint=(1, 0.15))
        self.add_widget(self.textbox)
        self.add_widget(self.boxlayout)
        self.boxlayout.add_widget(
            Button(on_release=Reminder.on_release, text="Tallenna", color=(0, 0, 0, 1))
        )

    def tallenna_merkinta(day, month, year, text):
        """Tallentaa (yrittää) merkinnän"""
        # Logics on pielessä. Ei pitäisi välittää tätä päivää, vaan valitun päivän date.
        print("yritetty tallentaa", day, month, year, text)
        # db.tee_merkinta(day, month, year, text)

    def on_release(self):
        """Kun valitaan joku päivä, tee popup"""
        print("Valittu päivä: ", self.text, Skeduler.month, Skeduler.year)
        if Reminder.tarkista_merkinta(self.text, Skeduler.month, Skeduler.year):
            self.background_color = (232 / 255, 123 / 255, 0, 0.5)

            # Tämä rakentaa pop-upin
        layout = BoxLayout(orientation="vertical")
        label = TextInput(text="fdafdsa")
        btn = Button(text="Tallenna", size_hint=(1, 0.20), color=(0, 0, 0, 1))
        layout.add_widget(label)
        layout.add_widget(btn)

        popup = Popup(
            title="Tallenna merkintä",
            title_color=(0, 0, 0, 1),
            content=layout,
            size_hint=(0.8, 0.8),
            background="images/tausta-lehdet.png",
        )

        def tallenna_helper(self):
            print("helper gets text:", label.text, self.text)
            self.rtext = label.text
            Reminder.tallenna(self.rtext)

        btn.bind(on_press=tallenna_helper)

        popup.open()

    def tarkista_merkinta(day: int, month: int, year=-1) -> bool:
        if year == -1:
            year = int(datetime.datetime.now().year)
            print("y:? ", year, end=" ")
        """Tarkistaa kalenterilta, onko päivämäärällä merkintää"""
        kakka = db.get_single_entry(day, month, year)
        if kakka:
            return True
        return False

    def tallenna(text):
        print("merkintä:", text, "pvm:")

    def closed(self, **kw):
        """Tähän tullaan, jos pop-up hylätään"""
        print("Dismissed :(")


class Skeduler(Screen):
    """Päivyrin pääluokka"""

    date = str(datetime.now().date().strftime("%d.%m.%Y"))  # PVM tänään

    now = datetime.now()  # Tämänhetkinen nykytilanne
    kk_nyt = calendar.monthcalendar(now.year, now.month)  # tämän kuukauden kk-kalenteri
    month = now.month
    year = now.year

    def __init__(self, **kw):
        super(Skeduler, self).__init__(**kw)

    def set_month(self, month):
        self.month = month
        if self.month < 1:
            self.year -= 1
            self.month = 12
            print("ylivuoto < ")
        elif self.month > 12:
            self.year += 1
            self.month = 1
            print("ylivuoto >")

        print("month set to", self.month)
        layout = Skeduler.draw_month(self.year, self.month)
        Dates.push_widget(layout)

    def get_month(self):
        return self.month

    def draw_month(self, month: int) -> GridLayout:
        # Tekee kalenterin päivistä (myös tyhjistä) nappuloita
        daylist = calendar.monthcalendar(Skeduler.now.year, month)
        layout = GridLayout()
        layout.cols = 7
        for days in daylist:
            for day in days:
                if day == 0:
                    layout.add_widget(Button(text=""))
                else:
                    ## !!! Jos päivällä on merkintä, niin vaihda myös taustaväri
                    if Reminder.tarkista_merkinta(day, month, Skeduler.year):
                        layout.add_widget(
                            Button(
                                text=str(day),
                                background_color=(128, 255, 0, 1),
                                color=(128, 0, 0, 1),
                                on_release=Reminder.on_release,
                            )
                        )
                    ## Jos merkintää ei ole .. niin taustaväriä ei vaihdeta
                    else:
                        layout.add_widget(
                            Button(
                                text=str(day),
                                color=(0, 0, 0, 1),
                                on_release=Reminder.on_release,
                            )
                        )
        return layout

    Builder.load_file("skeduler/skeduler.kv")


class Dates(GridLayout):
    """Yksittäisten päivien luokka"""

    now = Skeduler.now  # Nyt on nyt.
    cols = 7
    g = Skeduler.draw_month(now.year, now.month)

    def __init__(self, **kwargs):
        super(Dates, self).__init__(**kwargs)
        self.add_widget(Dates.g)
        global date_layout
        date_layout = self

    def push_widget(layout):
        global date_layout
        date_layout.clear_widgets()
        date_layout.add_widget(layout)
