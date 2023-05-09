from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.scrollview import MDScrollView
from kivy.properties import ObjectProperty


class ContentNavigationDrawer(MDScrollView):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class HH(MDApp):
    def build(self):
        return Builder.load_file("root.kv")


if __name__ == "__main__":
    HH().run()
