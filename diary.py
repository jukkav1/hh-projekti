from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.button import Button

kv = Builder.load_file("diary.kv")

class Diary(Screen):
    """päivyri"""

    Builder.load_file("diary/diary.kv")

    def write_diary(self):
        # Päivyrinäyttö
        date_dialog = Popup()
        date_dialog.add_widget(Button(text="tallenna", on_release=date_dialog.dismiss))
        date_dialog.open()

    def read_diary(self):
        self.ids.leibel.text = "lueskele"
