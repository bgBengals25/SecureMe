# Made by Luke Dinkler and Peter Toth

import Tkinter
from Tkinter import *

class InitGUI():

	def __init__(self):
		self.build()

	def build(self):
		self.root = Tk()
		self.root.geometry("500x400+300+300")
		self.root.title("SecureMe")

		self.root.mainloop()