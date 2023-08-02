from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout


class DatePicker(BoxLayout):
    """ " JEE"""

    def valitse_kuukausi(self, pvm):
        print("kakkaa: ", pvm)


KV = "datepicker.kv"
Builder.load_file(KV)
