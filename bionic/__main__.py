"""BIONIC main"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

from bionic.resources.elements import element_list


class ResourceButton(Button):
    """Resource button"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = 1, 1, 0, 1
        self.font_size = 70


class ResourceLayout(BoxLayout):
    """Resource layout"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        for element in element_list:
            self.add_widget(ResourceButton(text=element.__name__))


class BionicApp(App):
    """Bionic app"""

    def build(self):
        """Build app"""
        return ResourceLayout()


if __name__ == "__main__":
    BionicApp().run()
