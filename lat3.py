from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config
from kivy.core.window import Window

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.uix.button import Button

from kivy.graphics import Color, Rectangle

Builder.load_string('''
#:import hex kivy.utils.get_color_from_hex
<setScreen>:
    BoxLayout:
        orientation: 'vertical'
        spacing: 10
        canvas.before:
            Color:
                rgba: hex('006400')
            Rectangle:
                size: self.size
                pos: self.pos
        BoxLayout:
            orientation: 'horizontal'
            padding: 10
            spacing: 10
            Label:
                text: "Fake 24 Solver"
                font_size: 50
                bold: True
                italic: True
                pos_hint: {'center_x': -1, 'center_y': 0.65}
            BoxLayout:
                orientation: 'horizontal'
                padding: 5
                spacing: 20
                Image:
                    source: "deck.png"
                    width: 100
                    allow_stretch: False
                BoxLayout:
                    orientation: 'vertical'
                    padding: 10
                    spacing: 20
                    Button:
                        text: "DRAW and SOLVE!"
                    Button:
                        text: "Return to deck"
                    Button:
                        text: "Exit"
        BoxLayout:
            orientation: 'horizontal'
            padding: 20
            spacing: 30
            Image:
                source: "AC.png"
                width: 100
                allow_stretch: False
            Image:
                source: "AD.png"
                width: 100
                allow_stretch: False
            Image:
                source: "AH.png"
                width: 100
                allow_stretch: False
            Image:
                source: "AS.png"
                width: 100
                allow_stretch: False
        BoxLayout:
            orientation: 'horizontal'
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: "Solution:"
                    font_size: 20
                Label:
                    text: "//Solution//"
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: "Score:"
                    font_size: 20
                Label:
                    text: "//Score//"

''')

class setScreen(BoxLayout):
    pass

# Main Program
class Main(App):
    def build(self):
        return setScreen()

if __name__ == '__main__':
    Main().run()
