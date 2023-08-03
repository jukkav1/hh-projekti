from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen


class DatePickerContainer(Screen):
    pass


class DatePicker(BoxLayout):
    """ " JEE"""

    def valitse_kuukausi(self, pvm):
        print("kakkaa: ", pvm)


KV = "datepicker.kv"
Builder.load_file(KV)
