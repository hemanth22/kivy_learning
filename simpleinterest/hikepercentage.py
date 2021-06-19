import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('hike.kv')

class MyGridLayout(Widget):

    oldsalary = ObjectProperty()
    newsalary = ObjectProperty()

    def simpleiint(self):
        oldsalary = self.oldsalary.text
        newsalary = self.newsalary.text
        print('Your hike {0}%'.format(round((((int(newsalary)-int(oldsalary)) / int(oldsalary)) * 100),2)))
        self.oldsalary.text = ""
        self.newsalary.text = ""

class hikeApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    hikeApp().run()