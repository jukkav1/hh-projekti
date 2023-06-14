from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivymd.uix.pickers import MDDatePicker
from kivymd.app import MDApp
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

# class Diary(Screen):
#     """päivyri"""

#     Builder.load_file("kv/diary.kv")

#     def write_diary(self):
#         print("triggered kirjoita")
#         self.ids.leibel.text = "kirjoota"
#         pass

#     def read_diary(self):
#         print("triggered lueskelu!")
#         self.ids.leibel.text = "lueskele"


class Diary(Screen):
    Builder.load_file("kv/diary.kv")

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"

    def on_save(self, instance, value, date_range):
        """
        Events called when the "OK" dialog box button is clicked.

        :type instance: <kivymd.uix.picker.MDDatePicker object>;
        :param value: selected date;
        :type value: <class 'datetime.date'>;
        :param date_range: list of 'datetime.date' objects in the selected range;
        :type date_range: <class 'list'>;
        """
        print(instance, value, date_range)

    def on_cancel(self, instance, value):
        """Events called when the "CANCEL" dialog box button is clicked."""
        pass

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()
