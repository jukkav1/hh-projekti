from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen
import db.dbfunc as dbase


class DatePickerContainer(Screen):
    pass


class DatePicker(BoxLayout):
    """ " JEE"""

    def tee_merkinta(
        self, pvmlist, text="DatePicker class says henlo from datepicker.py!"
    ):
        pvm = pvmlist[0]
        kk = pvmlist[1]
        yy = pvmlist[2]
        d = self.tarkista_merkinta(pvm, kk, yy)
        if d:
            print(f"{pvm} {kk} {yy} on jo merkintä:", d)
        else:
            dbase.tee_merkinta(pvm, kk, yy, text)
            print(pvm, kk, yy, text)

    def tarkista_merkinta(self, pvm, kk, yy) -> list:
        merkintalista = dbase.hae_merkinta(pvm, kk, yy)
        print("merkintälista:", merkintalista)
        return merkintalista


KV = "kv/datepicker.kv"
Builder.load_file(KV)
