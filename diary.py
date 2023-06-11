from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.popup import Popup

from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class Diary(Screen):
    """päivyri"""

    Builder.load_file("kv/diary.kv")

    def write_diary(self):
        print("triggered kirjoita")
        self.ids.leibel.text = "kirjoota"
        pass

    def read_diary(self):
        print("triggered lueskelu!")
        self.ids.leibel.text = "lueskele"
