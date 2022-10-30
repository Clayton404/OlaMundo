from kivy.app import App
from kivy.uix.button import Button


class Testando(App):
	
	def build(self):
		
		return Button(text="Touch me" ,color=(1,1,1,1))

Testando().run()