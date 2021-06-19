import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('whatever.kv')

class MyGridLayout(Widget):

    name = ObjectProperty(None)
    pizza = ObjectProperty(None)
    color = ObjectProperty(None)
 
    def press(self):
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text
        #print(f'Hello {name}, your pizza {pizza} is getting ready in {color} colour')
        #self.add_widget(Label(text=f'Hello {name}, your {pizza} pizza is getting ready in {color} colour'))
        print(f'Hello {name}, your {pizza} pizza is getting ready in {color} colour')
        # Clear fields
        self.name.text = ""
        self.pizza.text = ""
        self.color.text = ""
        # Based on below class kivy file need to be created
        # Here App word should be excluded and create file my.kv
class AwesomeApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    AwesomeApp().run()