# Made by Luke Dinkler and Peter Toth

import Tkinter
from Tkinter import *
import ttk

class InitGUI():

	liberation_font_8 = ("Liberation Sans", 8)
	liberation_font_10 = ("Liberation Sans", 10)
	liberation_font_15 = ("Liberation Sans", 15)

	def __init__(self):
		self.build()

	def build(self):
		self.root = Tk()
		self.root.geometry("600x500+300+300")
		self.root.title("SecureMe")
		self.root.resizable(width=FALSE, height=FALSE)
		self.root.configure(font=self.liberation_font_10)

		self.notebook = ttk.Notebook(self.root, height=500)
		basicFrame = Frame(self.notebook)
		usersFrame = Frame(self.notebook)
		firewallFrame = Frame(self.notebook)
		updateFrame = Frame(self.notebook)
		self.notebook.add(basicFrame, text='Basic')
		self.notebook.add(usersFrame, text='Users')
		self.notebook.add(updateFrame, text='Updates')
		self.notebook.add(firewallFrame, text='Firewall')
		self.notebook.pack(fill=BOTH)

		basic_Label = Label(basicFrame, text='Basic Security Settings', font=self.liberation_font_15)
		basic_Label.pack()

		self.root.mainloop()