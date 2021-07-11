import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
#from kivy.uix.floatlayout import FloatLayout #use it if you are writing KV inside this python code

Builder.load_file('update_label.kv') #This will load any kind of kivy file not mandatory to follow class name in kivy

class MyLayout(Widget):
    def press(self):
        # Create variables for our widget
        name = self.ids.name_input.text
        # update the label
        self.ids.name_label.text = f'Hello {name}!'
        # clear the box
        self.ids.name_input.text = ''
        


class AwesomeApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    AwesomeApp().run()