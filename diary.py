from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

# päivyrimoduuli
from kivymd.uix.pickers import MDDatePicker


class Diary(Screen):
    """päivyri"""

    Builder.load_file("diary/diary.kv")

    def write_diary(self):
        # Päivyrinäyttö
        date_dialog = MDDatePicker()
        date_dialog.open()

    def read_diary(self):
        self.ids.leibel.text = "lueskele"
