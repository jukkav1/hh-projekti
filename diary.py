from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.popup import Popup

# from kivy.uix.button import Button
# from kivy.uix.textinput import TextInput


class Diary(Screen):
    """päivyri"""

    Builder.load_file("kv/diary.kv")

    def write_diary(self):
        # Päivyrinäyttö
        date_dialog = Poppi()
        # date_dialog.add_widget(Button(text="tallenna", on_release=date_dialog.dismiss))
        date_dialog.open()

    def read_diary(self):
        self.ids.leibel.text = "lueskele"


class Poppi(Popup):
    def tallenna(self):
        print("koitetaan tallentaa")
        self.dismiss()
