import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
	# initialize inifinte keyword
	def __init__(self, **kwargs):
		# call grid layout constructor
		super(MyGridLayout, self).__init__(**kwargs)

		# Set columns 
		self.cols = 1
		# Create a second layout
		self.top_grid = GridLayout()
		self.top_grid.cols = 2


		# Add widgets
		self.top_grid.add_widget(Label(text="Name: ",size_hint_y=None,height=50,size_hint_x=None,width=200))
		# Add Input Box
		self.name = TextInput(multiline=False,size_hint_y=None,height=50,size_hint_x=None,width=400)
		self.top_grid.add_widget(self.name)


		# Add widgets
		self.top_grid.add_widget(Label(text="Favorite Pizza: "))
		# Add Input Box
		self.pizza = TextInput(multiline=False)
		self.top_grid.add_widget(self.pizza)


		# Add widgets
		self.top_grid.add_widget(Label(text="Favorite color: "))
		# Add Input Box
		self.color = TextInput(multiline=False)
		self.top_grid.add_widget(self.color)

		# Add the new top_grid to our app
		self.add_widget(self.top_grid)

		#Create a Submit Button
		self.submit = Button(text="Submit", font_size=32, size_hint_y=None, height=50, size_hint_x=None, width=200)
		# Bind the button
		self.submit.bind(on_press=self.press)
		self.add_widget(self.submit)

	def press(self, instance):
		name = self.name.text
		pizza = self.pizza.text
		color = self.color.text
		#print(f'Hello {name}, your pizza {pizza} is getting ready in {color} colour')
		self.add_widget(Label(text=f'Hello {name}, your {pizza} pizza is getting ready in {color} colour'))
		# Clear fields
		self.name.text = ""
		self.pizza.text = ""
		self.color.text = ""

class MyApp(App):
	def build(self):
		return MyGridLayout()

if __name__ == '__main__':
	MyApp().run()