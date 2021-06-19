import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

#Builder.load_file('whatever.kv') #This will load any kind of kivy file not mandatory to follow class name in kivy
Builder.load_string("""

<MyGridLayout>

    name:name
    pizza:pizza
    color:color

    GridLayout:
        cols:1
        size: root.width, root.height
        GridLayout:
            cols:2

            Label:
                text: "Name"
            TextInput:
                id: name
                multiline:False

            Label:
                text: "Favorite Pizza"
            TextInput:
                id: pizza
                multiline:False

            Label:
                text: "Favorite color"
            TextInput:
                id: color
                multiline:False

        Button:
            text: "Submit"
            font_size: 32
            on_press: root.press()
    """)

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