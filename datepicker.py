from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout


class DatePicker(BoxLayout):
    pass


KV = "datepicker.kv"
Builder.load_file(KV)
