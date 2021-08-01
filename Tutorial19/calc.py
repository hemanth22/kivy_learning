import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
#from kivy.uix.floatlayout import FloatLayout #use it if you are writing KV inside this python code

#Set the app size
Window.size = (500,700)

Builder.load_file('calc.kv') #This will load any kind of kivy file not mandatory to follow class name in kivy

class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = '0'
    
    def button_press(self, button):
        prior = self.ids.calc_input.text
        
        if "Error" in prior:
            prior = ''

        if prior == "0":
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text = f'{prior}{button}'


    def remove(self):
        prior = self.ids.calc_input.text
        prior = prior[:-1]
        self.ids.calc_input.text = prior

    def pos_neg(self):
        prior = self.ids.calc_input.text
        if "-" in prior:
            self.ids.calc_input.text = f'{prior.replace("-","")}'
        else:
            self.ids.calc_input.text = f'-{prior}'
        
    def dot(self):
        prior = self.ids.calc_input.text
        num_list = prior.split("+")
        
        if "+" in prior and "." not in num_list[-1]:
            prior = f'{prior}.'
            self.ids.calc_input.text = prior

        elif "." in prior:
            pass
        else:
            prior = f'{prior}.'
            self.ids.calc_input.text = prior
            
    def math_sign(self, sign):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}{sign}'      

    def equals(self):
        prior = self.ids.calc_input.text
        try:
            answer = eval(prior)
            self.ids.calc_input.text  = str(answer)
        except:
            self.ids.calc_input.text  = "Error"
        '''
        if "+" in prior:
            num_list = prior.split("+")
            #print(num_list)
            answer = 0.0
            for number in num_list:
                answer = answer + float(number)
                #print(answer)
                self.ids.calc_input.text = str(answer)
        '''

class CalculatorApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    CalculatorApp().run()