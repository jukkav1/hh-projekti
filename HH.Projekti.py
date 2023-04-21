import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.image import Image


class MyGrid(GridLayout):
    def __init__(self, kwargs):
        super(MyGrid, self).init(kwargs)
        pass


class MainBacground(Widget):
    def __init__(self, **kwargs):
        super(MainBacground, self).__init__(**kwargs)
        pass


class HH(App):
    def build(self):
        return MainBacground()


if __name__ == "__main__":
    HH().run()
