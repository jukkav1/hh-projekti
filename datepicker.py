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

    def tee_merkinta(self, pvmlist):
        pvm = pvmlist[0]
        kk = pvmlist[1]
        yy = pvmlist[2]
        if self.tarkista_merkinta(pvm, kk, yy):
            print("On jo merkintä tai joku vika.")

        else:
            dbase.tee_merkinta(pvm, kk, yy)
            print("tehtiin merkintä.")

    def tarkista_merkinta(self, pvm, kk, yy) -> list:
        merkintalista = dbase.hae_merkinta(pvm, kk)
        print("merkintälista:", merkintalista)
        return merkintalista


KV = "kv/datepicker.kv"
Builder.load_file(KV)
