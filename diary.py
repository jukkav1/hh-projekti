from kivy.uix.screenmanager import Screen
from kivy.lang import Builder


class Diary(Screen):
    """päivyri"""

    Builder.load_file("diary/diary.kv")

    def write_diary(self):
        self.ids.leibel.text = "kirjoittele"

    def read_diary(self):
        self.ids.leibel.text = "lueskele"
