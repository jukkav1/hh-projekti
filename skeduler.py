# Project made by: Kuldeep Singh
# Student at LNMIIT,Jaipur,India;

# Typos, python3 etc fixes and further dev by:
# Jukka Valvanne

# import statements
import calendar
import time
import datetime
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ListProperty
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen
from db.dbfunc import *
from random import randint
from kivy.uix.widget import Widget

# loaderit kivy-fileille
Builder.load_file("skeduler/months.kv")  # kuukaudet
Builder.load_file("skeduler/dates.kv")  # päivämäärät
Builder.load_file("skeduler/status.kv")  # tila-aika-jatkumo
Builder.load_file("skeduler/days.kv")  # viikonpäivät


# Skeleton luokat
# ---------------------------#
# class Calendar(BoxLayout):
#     """Kalenterin pääluokka"""

#     def __init__(self, **kwargs):
#         super(Calendar, self).__init__(**kwargs)


class Status(BoxLayout):
    """Status -palkin luokka"""

    def __init__(self, **kwargs):
        super(Status, self).__init__(**kwargs)


class Months(BoxLayout):
    """Kuukausilistan luokka"""

    def __init__(self, **kwargs):
        super(Months, self).__init__(**kwargs)

    def valitse_kuukausi(self, mo):
        print("Valitsit kuukauden ", mo)
        Skeduler.set_month(Skeduler, mo)
        w = Skeduler.draw_month(Skeduler.now.year, Skeduler.month)
        Dates.push_widget(self, w)


# ------------------------------------------------------------------------------------------------#


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
            Button(on_release=self.on_release, text="Tallenna", color=(0, 0, 0, 1))
        )

    def on_release(self, event):
        """Tallennusta painettu, pitäisi kutsua tallennusfunktiota ja sulkea pop-up!"""
        # print("Yritetty tallentaa", self.textbox.text)

        # Logics on pielessä, ei pitäisi välittää tätä päivää, vaan valitun päivän date.
        self.tallenna_merkinta(self.textbox.text, Dates.now.month, Dates.now)

    def tallenna_merkinta(text, month, now):
        # Logics on pielessä. Ei pitäisi välittää tätä päivää, vaan valitun päivän date.
        """Tallentaa (yrittää) merkinnän"""
        print("yritetty tallentaa", now, month, text)
        tee_merkinta(now, month, text)
        test_connection()

    # Tänne tullaan, jos
    def on_release(self, event):
        """Kun valitaan joku päivä, tee popup"""
        print("Valittu päivä: ", event.text, self.now.month, self.now.year)
        if self.tarkista_merkinta(event.text, self.now.month):
            event.background_color = (232 / 255, 123 / 255, 0, 0.5)

            # Tämä rakentaa pop-upin
        self.popup = Popup(
            title="Tee merkintä",
            title_color=(0, 0, 0, 1),
            title_align="center",
            background="images/tausta-lehdet.png",
            content=Reminder(),
            size_hint=(None, None),
            size=(self.width * 3 / 4, self.height),
        )
        # Jos popup escataan, mene on_dismiss -funktioon.
        self.popup.bind(on_dismiss=self.on_dismiss)

        # avaa se popup
        self.popup.open()

    def tarkista_merkinta(day, month):
        kakka = randint(0, 1)
        if kakka:
            return True
        return False

    def on_dismiss(self, event):
        """Tähän tullaan, jos pop-up hylätään"""
        print("Dismissed :(")


# mainApp class
class Skeduler(Screen):
    """Päivyrin pääluokka"""

    now = datetime.datetime.now()  # Nyt on nyt.
    kk_nyt = calendar.monthcalendar(now.year, now.month)
    month = now.month

    def __init__(self, **kw):
        super(Skeduler, self).__init__(**kw)

    def set_month(self, month):
        self.month = month
        print("month set to", self.month)
        Skeduler.draw_month(Dates, self.month)

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
                    if Reminder.tarkista_merkinta(day, month):
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

    def __init__(self, **kwargs):
        super(Dates, self).__init__(**kwargs)
        piirra_nyt = Skeduler.draw_month(self.now.year, self.now.month)
        self.add_widget(piirra_nyt)

    def push_widget(self, s):
        print(s)
        g = Skeduler.draw_month(Skeduler.now.year, Skeduler.month)
        self.remove_widget(g)
        self.add_widget(g)
