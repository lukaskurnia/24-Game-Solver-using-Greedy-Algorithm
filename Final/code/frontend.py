import backend
import random

from kivy.app import App
from kivy.lang import Builder

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.text import LabelBase
from kivy.uix.textinput import TextInput

from kivy.uix.boxlayout import BoxLayout

#from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.uix.button import Button

from kivy.graphics import Color, Rectangle

# Tampilan frontend
Builder.load_string('''
#:import hex kivy.utils.get_color_from_hex
<Login>:
    BoxLayout:
        orientation: 'vertical'
        padding : 30, 30
        canvas.before:
            Color:
                rgba: hex('006400')
            Rectangle:
                size: self.size
                pos: self.pos
        Label:
            text: "Fake 24 Solver"
            font_size: 70
            bold: True
            italic: True
            pos_hint: {'center_x': 0.5, 'center_y': 0.65}
        BoxLayout:
            orientation: "horizontal"
            padding: 10, 10
            spacing: 10, 10
            size_hint_x: .7
            canvas.before:
                Color:
                    rgba: hex('006400')
                Rectangle:
                    size: self.size
                    pos: self.pos
            Label:
                text: "Username   "
                text_size: self.size
                halign: 'right'
                size_hint_x: .5
                size_hint_y: .3
                pos_hint: {'center_x': 0.7, 'center_y': 0.79}

            TextInput:
                multiline: False
                size_hint_x: .5
                size_hint_y: .15
                pos_hint: {'center_x': 0.4, 'center_y': 0.65}
                id : tester
        Button:
            text: 'LOGIN'
            padding: 200, 200
            spacing: 10, 10
            valign: 'middle'
            size_hint_x: .2
            size_hint_y: .2
            pos_hint: {'center_x': 0.5, 'center_y': 0.8}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.current = 'Play'
                root.login()
        Button:
            text: 'Quit'
            padding: 100, 100
            spacing: 10, 10
            size_hint_x: .2
            size_hint_y: .2
            pos_hint: {'center_x': 0.5, 'center_y': 0.8}
            on_press: app.stop()

<Play>:
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
            BoxLayout:
                orientation: 'vertical'
                Label:
                    id: title
                    text: ""
                    font_size: 50
                    bold: True
                    italic: True
                Label:
                    id: cards
                    text: "Cards remaining: 52"
            BoxLayout:
                orientation: 'horizontal'
                padding: 5
                spacing: 20
                Image:
                    source: "../resource/deck.png"
                    width: 100
                    allow_stretch: False
                BoxLayout:
                    orientation: 'vertical'
                    padding: 10
                    spacing: 20
                    Button:
                        text: "DRAW and SOLVE!"
                        bold: True
                        on_press: root.DaS()
                    Button:
                        text: "Return to deck"
                        bold: True
                        on_press: root.rebound()
                    Button:
                        text: "Exit"
                        bold: True
                        on_press: app.stop()
        BoxLayout:
            orientation: 'horizontal'
            padding: 20
            spacing: 30
            Image:
                source: "../resource/blue_back.png"
                width: 100
                allow_stretch: False
                id: pic1
            Image:
                source: "../resource/gray_back.png"
                width: 100
                allow_stretch: False
                id: pic2
            Image:
                source: "../resource/red_back.png"
                width: 100
                allow_stretch: False
                id: pic3
            Image:
                source: "../resource/yellow_back.png"
                width: 100
                allow_stretch: False
                id: pic4
        BoxLayout:
            orientation: 'horizontal'
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: "Solution :"
                    font_size: 35
                    bold: True
                Label:
                    text: ""
                    id: solution
            BoxLayout:
                orientation: 'horizontal'
                BoxLayout:
                    orientation: 'vertical'
                    Label:
                        text: "Result :"
                        font_size: 35
                        bold: True
                    Label:
                        text: ""
                        id: result
                BoxLayout:
                    orientation: 'vertical'
                    Label:
                        text: "Score :"
                        font_size: 35
                        bold: True
                    Label:
                        text: ""
                        id: score
''')

# List deck kartu
deck = [True] * 52

# Nama pemain
name = [""] * 2

#class Screen1(BoxLayout):
class Login(Screen):
    def login(self):
        name[0] = self.ids.tester.text


class Play(Screen):
    def on_enter(self):
        self.ids.title.text = name[0]
        print(self.ids.title.text)
    def DaS(self):
        if countDeck() == 0:
            self.ids.solution.text = "Fail, no solution"
            self.ids.score.text = "Empty deck"
        else:
            cards = randomizer()
            print("Cards:", end='')
            print(cards)
            print("Remaining cards:", end='')
            print(countDeck())
            # Gambarkan pada kartu
            picList = drawCards(cards)
            print("Pictures:", end='')
            print(picList)
            self.ids.pic1.source = picList[0]
            self.ids.pic2.source = picList[1]
            self.ids.pic3.source = picList[2]
            self.ids.pic4.source = picList[3]

            # Mencari solusi
            mapNumbers(cards)
            print("Numbers:", end='')
            print(cards)
            solution = backend.algorithm24(cards)
            score = backend.score24(solution)
            self.ids.solution.text = solution
            self.ids.result.text = str(eval(solution))
            self.ids.score.text = str(score)
            self.ids.cards.text = "Cards remaining = " + str(len(deck))

    def rebound(self):
        for i in range(len(deck)):
            deck[i] = True
        self.ids.pic1.source = "../resource/blue_back.png"
        self.ids.pic2.source = "../resource/gray_back.png"
        self.ids.pic3.source = "../resource/red_back.png"
        self.ids.pic4.source = "../resource/yellow_back.png"
        print("Remaining cards:", end='')
        print(countDeck())

# DRAW and SOLVE
def countDeck():
    count = 0
    for i in range(len(deck)):
        if deck[i] == True:
            count += 1
    return count

def randomizer():
    cards = []
    for i in range(0, 4):
        found = False
        while not found:
            x = random.randint(0, 51)
            if (deck[x] == True):
                deck[x] = False
                found = True
                cards.append(x)
    return cards

def mapNumbers(cards):
    for i in range(len(cards)):
        cards[i] = int(cards[i]) % 13
        if (cards[i]) == 0:
            cards[i] = 13

def drawCards(cards):
    picList = []
    for i in range(len(cards)):
        num = int(cards[i]) % 13
        sign =int(cards[i]) // 13
        picList.append(mapping(num, sign))
    return picList

def mapping(num, sign):
    target = "../resource/"
    # Nomor kartu
    if num == 1:
        target += "A"
    elif num == 11:
        target += "J"
    elif num == 12:
        target += "Q"
    elif num == 0:
        target += "K"
    else:
        target += str(num)
    # Simbol kartu
    if sign == 0:
        target += "D"
    elif sign == 1:
        target += "C"
    elif sign == 2:
        target += "H"
    elif sign == 3:
        target += "S"

    target += ".png"
    return target

sm = ScreenManager()
sm.add_widget(Login(name='Login'))
sm.add_widget(Play(name='Play'))
# Main Program
class Main(App):
    def build(self):
        return sm #Play()

if __name__ == '__main__':
    Main().run()
