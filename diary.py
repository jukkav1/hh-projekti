from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

kv = Builder.load_file("diary.kv")

class Diary(Screen):
    """päivyri"""
    def build(self):
        return kv