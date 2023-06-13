from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton


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

    def build(self):
        return MDScreen(
            MDRaisedButton(
                text="Open data picker",
                pos_hint={"center_x": 0.5, "center_y": 0.5},
                on_release=self.show_date_picker,
            )
        )

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

    def show_date_picker(self, *args):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()
