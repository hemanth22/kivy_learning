import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
#from kivy.uix.floatlayout import FloatLayout #use it if you are writing KV inside this python code

Builder.load_file('float_layout.kv') #This will load any kind of kivy file not mandatory to follow class name in kivy

class MyLayout(Widget):
    pass


class AwesomeApp(App):
    def build(self):
        Window.clearcolor = (1,1,1,1)
        return MyLayout()

if __name__ == '__main__':
    AwesomeApp().run()