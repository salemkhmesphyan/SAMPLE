from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.splitter import Splitter
from kivy.uix.switch import Switch
class MainApp(App):
	def build(self):
		main_layout = BoxLayout(orientation="vertical",size_hint=(1, 1))
		main_layout1 =Splitter(sizable_from = 'left',strip_size = '10pt')
		s=Switch(active=False)
		
		self.solution = TextInput(multiline=True,  halign="left", font_size=20)
		main_layout1.add_widget(self.solution)
		equals_button = Button(text="=", pos_hint={"center_x": 0.5, "center_y": 0.5})
		equals_button.bind(on_press=self.dd)
		main_layout.add_widget(main_layout1)
		main_layout.add_widget(equals_button)
		main_layout.add_widget(s)
		return main_layout
	def dd(self,instance):
		text1=str(self.solution.text)
		self.solution.text=str(eval(text1))
		print("hgiigiug")
if __name__ == "__main__":
    app = MainApp()
    app.run()
