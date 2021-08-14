from kivy.config import Config

Config.set('graphics', 'position', 'custom')

Config.set('graphics', 'fullscreen', 'real')

Config.set('graphics', 'top', '100')

Config.set('graphics', 'left', '100')

Config.set('graphics', 'resizable', True)

from kivy.app import App

from kivy.uix.label import Label

from kivy.core.window import Window

# Window.size = (600, 300)

from kivy.uix.widget import Widget

from kivy.uix.boxlayout import BoxLayout

from kivy.uix.textinput import TextInput

from kivy.uix.button import Button

from kivy.uix.floatlayout import FloatLayout

from kivy.graphics import Color, Ellipse, Line,Rectangle

from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.uix.relativelayout import RelativeLayout

from kivy.uix.image import Image

import win32gui

import win32con

import win32api,pywintypes

import win32gui

import win32con

import win32api,pywintypes

Window.size = (600, 600)

class Program(App):

    def on_start(self):

        hwnd = win32gui.FindWindow(None, "pencere 2.0")

        win32gui.SetWindowLong(hwnd,win32gui.GetWindowLong(hwnd,win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)

        win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(255, 255, 128),40, win32con.LWA_ALPHA)

    def build(self):

        sm = ScreenManager()

        duzen = FloatLayout()

        screen = Screen(name='SSS')

        self.title = "pencere 2.0"

        yazi = Label(text = self.title,pos=(10,10),size=(100,35),size_hint=(None,None),halign="center",bold=True,color=(1,0,0,1))

        buton = Button(text="",size_hint=(None,None),size=(26,26))

        buton.pos = (0,0)

        buton.background_normal = "minimize.png"

        buton.background_down = "minimize.png"

        with Window.canvas:

            Color(0,0,0,1)

        Rectangle(pos=(10, 10), size=(100, 40))

        duzen.add_widget(yazi)

        for child in Window.children:

            print("Cocuk : "+child)

        return duzen

Program().run()