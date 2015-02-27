# Made by Luke Dinkler and Peter Toth

import Tkinter
from Tkinter import *
import ttk
from getrtpwd import RootPasswordWindow
import os, sys
from text import CustomText
os.system('cd ..')
from src.securityfunctions.admin import *
from src.securityfunctions.firewall import *
from src.securityfunctions.guest import *
from src.securityfunctions.rootpassencryption import *
from src.securityfunctions.update import *
from src.securityfunctions.users import *
from src.securityfunctions.service import Services

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

		menubar = Menu(self.root)
		optionsmenu = Menu(menubar)
		optionsmenu.add_command(label="Refresh", command=lambda : self.refresh())
		optionsmenu.add_command(label="Exit", command=sys.exit)
		menubar.add_cascade(label="Options", menu=optionsmenu)
		self.root.config(menu=menubar)

		self.notebook = ttk.Notebook(self.root, height=500)
		basicFrame = Frame(self.notebook)
		usersFrame = Frame(self.notebook, padx=25, pady=25)
		firewallFrame = Frame(self.notebook)
		updateFrame = Frame(self.notebook)
		servicesFrame = Frame(self.notebook, padx=25, pady=25)
		self.notebook.add(basicFrame, text='Basic')
		self.notebook.add(usersFrame, text='Users')
		self.notebook.add(updateFrame, text='Updates')
		self.notebook.add(firewallFrame, text='Firewall')
		self.notebook.add(servicesFrame, text='Services')
		self.notebook.pack(fill=BOTH)

		# Basic Panel
		basic_label = Label(basicFrame, text='Basic Security Settings', font=self.liberation_font_15)
		basic_label.pack()
		basic_update = Button(basicFrame, text='Basic Update', command=lambda : self.basicUpdate())
		basic_update.pack(padx=10, pady=10)

		# Users Panel
		users_label = Label(usersFrame, text='User Security Settings', font=self.liberation_font_15)
		users_label.pack()

		userpanel = LabelFrame(usersFrame, text="Users", padx=10, pady=10)
		userpanel.pack(side=TOP, fill=BOTH)

		self.uText = self.getUserText()
		self.users_listlabel = Label(userpanel, text=self.uText, padx=10, pady=10)
		self.users_listlabel.pack(side=LEFT)

		groupspanel = LabelFrame(usersFrame, text="Groups", padx=10, pady=10)
		groupspanel.pack(side=TOP, fill=BOTH)

		self.gText = self.getGroupText()
		self.groups_text = CustomText(groupspanel)
		self.groups_text.resetText(self.gText)
		self.groups_text.type(DISABLED)
		self.groups_text.pack(fill=BOTH)

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

		# Services Pane
		servicespanel = LabelFrame(servicesFrame, text="Services", padx=10, pady=10)
		servicespanel.pack(side=TOP, fill=BOTH)
		self.sText = self.getServicesText()
		self.services_text = CustomText(servicespanel)
		self.services_text.resetText(self.sText)
		self.services_text.type(DISABLED)
		self.services_text.pack(fill=BOTH)


		self.root.mainloop()

	def refresh(self):
		self.uText = self.getUserText()
		self.gText = self.getGroupText()
		self.users_listlabel.config(text=self.uText)
		self.groups_text.type(NORMAL)
		self.groups_text.resetText(self.gText)
		self.groups_text.type(DISABLED)

	def getPassword(self):
		pwd = self.enc.decrypt()
		return pwd

	def getUserText(self):
		u = Users()
		retstr = u.getUsers()
		ret = ''
		for i in retstr:
			ret += "User: " + i + "\n"
		return ret

	def getGroupText(self):
		g = Groups()
		retstr = g.getGroups()
		ret = ''
		for i in retstr:
			ret += i + "\n"
		return ret

	def getServicesText(self):
		s = Services()
		retstr = s.getservicesbasic()
		return retstr

	def basicUpdate(self):
		ud = Update()
		ud.update(self.enc)

	def enableFirewall(self):
		f = Firewall()
		f.enable(self.getPassword())

	def disableFirewall(self):
		f = Firewall()
		f.disable(self.getPassword())