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

		# Basic Panel
		basic_label = Label(basicFrame, text='Basic Security Settings', font=self.liberation_font_15)
		basic_label.pack()

		# Users Panel
		users_label = Label(usersFrame, text='User Security Settings', font=self.liberation_font_15)
		users_label.pack()

		# Firewall Label
		firewall_label = Label(firewallFrame, text='Firewall Settings', font=self.liberation_font_15)
		firewall_label.pack()

		edFrame = Frame(firewallFrame)
		fwEnable = Button(edFrame, text='Enable')
		fwEnable.pack(side=LEFT, padx=10, pady=10)
		fwDisable = Button(edFrame, text='Disable')
		fwDisable.pack(side=RIGHT, padx=10, pady=10)
		edFrame.pack()

		# Update Label
		update_label = Label(updateFrame, text='System Updates', font=self.liberation_font_15)
		update_label.pack()

		self.root.mainloop()