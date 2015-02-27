# Made by Luke Dinkler and Peter Toth

import Tkinter
from Tkinter import *
import ttk
from getrtpwd import RootPasswordWindow
import os, sys
os.system('cd ..')
from src.securityfunctions.admin import *
from src.securityfunctions.firewall import *
from src.securityfunctions.guest import *
from src.securityfunctions.rootpassencryption import *
from src.securityfunctions.update import *
from src.securityfunctions.users import *

class InitGUI():

	liberation_font_8 = ("Liberation Sans", 8)
	liberation_font_10 = ("Liberation Sans", 10)
	liberation_font_15 = ("Liberation Sans", 15)

	def __init__(self):
		self.enc = Encryption()
		self.grp = RootPasswordWindow(self.enc)
		self.build()

	def build(self):
		self.root = Tk()
		self.root.geometry("500x400+300+300")
		self.root.title("SecureMe")
		self.root.resizable(width=FALSE, height=FALSE)

		# Menubar
		menubar = Menu(self.root)
		options = Menu(menubar, tearoff=0)
		options.add_command(label="Refresh", command=lambda : self.refresh())
		options.add_command(label="Exit", command=lambda : sys.exit(0))
		menubar.add_cascade(label="Options", menu=options)
		self.root.configure(menu=menubar)

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
		basic_update = Button(basicFrame, text='Basic Update', command=lambda : self.basicUpdate())
		basic_update.pack(padx=10, pady=10)

		# Users Panel
		usersFrame.config(padx=25, pady=25)
		users_label = Label(usersFrame, text='User Security Settings', font=self.liberation_font_15)
		users_label.pack()

		userpanel = LabelFrame(usersFrame, text="Users", padx=10, pady=10)
		userpanel.pack(side=TOP, fill=BOTH)

		self.uText = self.getUserText()
		self.users_listlabel = Label(userpanel, text=self.uText, padx=10, pady=10)
		self.users_listlabel.pack(side=LEFT)

		grouppanel = LabelFrame(usersFrame, text='Groups', padx=10, pady=10)
		grouppanel.pack(side=TOP, fill=BOTH)

		self.gText = self.getGroupText()
		self.groups_listtext = Text(grouppanel, padx=10, pady=10)
		self.groups_listtext.insert(END, self.gText)
		self.groups_listtext.config(state=DISABLED)
		self.groups_listtext.pack(side=LEFT, fill=BOTH)

		# Firewall Label
		firewall_label = Label(firewallFrame, text='Firewall Settings', font=self.liberation_font_15)
		firewall_label.pack()

		edFrame = Frame(firewallFrame)
		fwEnable = Button(edFrame, text='Enable', command=lambda : self.enableFirewall())
		fwEnable.pack(side=LEFT, padx=10, pady=10)
		fwDisable = Button(edFrame, text='Disable', command=lambda : self.disableFirewall())
		fwDisable.pack(side=RIGHT, padx=10, pady=10)
		edFrame.pack()

		# Update Label
		update_label = Label(updateFrame, text='System Updates', font=self.liberation_font_15)
		update_label.pack()

		update_button = Button(updateFrame, text='Standard Update', font=self.liberation_font_10)

		self.root.mainloop()

	def refresh(self):
		self.uText = self.getUserText()
		self.gText = self.getGroupText()
		self.users_listlabel.configure(text=self.uText)
		self.groups_listtext.delete("1.0", END)

	def getPassword(self):
		pwd = self.enc.decrypt()
		return pwd

	def getUserText(self):
		u = Users()
		retstr = u.getUsers()
		ret = ''
		for i in retstr:
			ret += i + "\n"
		return ret

	def getGroupText(self):
		g = Groups()
		retstr = g.getGroups()
		ret = ''
		for i in retstr:
			ret += i + "\n"
		print(ret)
		return ret

	def basicUpdate(self):
		ud = Update()
		ud.update(self.enc)

	def enableFirewall(self):
		f = Firewall()
		f.enable(self.getPassword())

	def disableFirewall(self):
		f = Firewall()
		f.disable(self.getPassword())