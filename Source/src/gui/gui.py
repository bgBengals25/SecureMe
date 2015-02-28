# Made by Luke Dinkler and Peter Toth

import Tkinter, tkMessageBox
from Tkinter import *
import ttk
from ttk import Style
from getrtpwd import RootPasswordWindow
import os, sys, time
import threading
from threading import Thread
from text import CustomText
from toolbar import ToolBar
os.system('cd ..')
from src.securityfunctions.admin import *
from src.securityfunctions.firewall import *
from src.securityfunctions.guest import *
from src.securityfunctions.rootpassencryption import *
from src.securityfunctions.update import *
from src.securityfunctions.users import *
from src.securityfunctions.service import Services
from src.securityfunctions.processes import Processes

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
		self.root.geometry("800x622+200+200")
		self.root.title("SecureMe")
		#self.root.resizable(width=FALSE, height=FALSE)
		self.root.configure(bg="slate gray")

		menubar = Menu(self.root)
		optionsmenu = Menu(menubar, tearoff=0)
		optionsmenu.add_command(label="Refresh (Ctrl+r)", command=lambda : self.refresh("NONE"))
		optionsmenu.add_command(label="Exit", command=lambda : self.quitMenu())
		menubar.add_cascade(label="Options", menu=optionsmenu)
		self.root.config(menu=menubar)

		self.toolbar = ToolBar(self.root, self)

		style = Style()
		style.configure("BW.TLabel", foreground="black", background="slate gray", borderwidth=2)

		mFrame = Frame(self.root, bg="slate gray", padx=25, pady=25)
		mFrame.pack(fill=BOTH)
		self.notebook = ttk.Notebook(mFrame, height=500, style="BW.TLabel")
		primaryFrame = Frame(self.notebook, padx=25, pady=25)
		usersFrame = Frame(self.notebook, padx=25, pady=25)
		firewallFrame = Frame(self.notebook, padx=25, pady=25)
		updateFrame = Frame(self.notebook, padx=25, pady=25)
		servicesFrame = Frame(self.notebook, padx=25, pady=25)
		processesFrame = Frame(self.notebook, padx=25, pady=25)
		self.notebook.add(primaryFrame, text='Primary')
		self.notebook.add(usersFrame, text='Users')
		self.notebook.add(updateFrame, text='Updates')
		self.notebook.add(firewallFrame, text='Firewall')
		self.notebook.add(servicesFrame, text='Services')
		self.notebook.add(processesFrame, text='Processes')
		self.notebook.pack(fill=X)

		self.updatebar = Frame(self.root)
		self.updatebar.pack(side=BOTTOM, fill=X)
		self.left_label = Label(self.updatebar, text="Current Process: None")
		self.left_label.pack(side=LEFT, fill=X)

		# Primary Panel
		primary_label = Label(primaryFrame, text='Primary Settings', font=self.liberation_font_15)
		primary_label.pack()

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
		fwEnable.pack(side=LEFT, padx=10, pady=10, fill=X)
		fwDisable = Button(edFrame, text='Disable', command=lambda : self.disableFirewall())
		fwDisable.pack(side=RIGHT, padx=10, pady=10, fill=X)
		edFrame.pack()

		firewallpanel = LabelFrame(firewallFrame, text='Firewall Status', height=100, width=450, padx=10, pady=10)
		firewallpanel.pack(side=TOP, fill=X)

		self.fText = self.getFirewallStatus()
		self.firewall_text = CustomText(firewallpanel)
		self.firewall_text.resetText(self.fText)
		self.firewall_text.type(DISABLED)
		self.firewall_text.pack(fill=X)

		# Update Label
		update_label = Label(updateFrame, text='System Updates', font=self.liberation_font_15)
		update_label.pack()

		update_button = Button(updateFrame, text='Basic Update', command=lambda : self.basicUpdate())
		update_button.pack(padx=10, pady=10)

		upgrade_button = Button(updateFrame, text='Basic Upgrade', command=lambda : self.basicUpgrade())
		upgrade_button.pack(padx=10, pady=10)

		packageupdate_button = Button(updateFrame, text='Package Update', command=lambda : self.packageUpdate())
		packageupdate_button.pack(padx=10, pady=10)

		# Services Pane
		services_label = Label(servicesFrame, text='System Services', font=self.liberation_font_15)
		services_label.pack()

		servicespanel = LabelFrame(servicesFrame, text="Services", padx=10, pady=10)
		servicespanel.pack(side=TOP, fill=BOTH)
		self.sText = self.getServicesText()
		self.services_text = CustomText(servicespanel)
		self.services_text.resetText(self.sText)
		self.services_text.type(DISABLED)
		self.services_text.pack(fill=BOTH)

		# Processes Pane
		processes_label = Label(processesFrame, text='System Processes', font=self.liberation_font_15)
		processes_label.pack()

		processespanel = LabelFrame(processesFrame, text='Processes', padx=10, pady=10)
		processespanel.pack(side=TOP, fill=BOTH)
		self.pText = self.getProcessesText()
		self.processes_text = CustomText(processespanel)
		self.processes_text.resetText(self.pText)
		self.processes_text.type(DISABLED)
		self.processes_text.pack(fill=BOTH)

		self.root.bind('<Control-r>', self.refresh)

		self.root.mainloop()

	def refresh(self, e):
		self.setLeftLabel("Refreshing...")
		self.uText = self.getUserText()
		self.gText = self.getGroupText()
		self.sText = self.getServicesText()
		self.fText = self.getFirewallStatus()
		self.pText = self.getProcessesText()
		self.users_listlabel.config(text=self.uText)
		self.groups_text.type(NORMAL)
		self.groups_text.resetText(self.gText)
		self.groups_text.type(DISABLED)
		self.services_text.type(NORMAL)
		self.services_text.resetText(self.sText)
		self.services_text.type(DISABLED)
		self.firewall_text.type(NORMAL)
		self.firewall_text.resetText(self.fText)
		self.firewall_text.type(DISABLED)
		self.processes_text.type(NORMAL)
		self.processes_text.resetText(self.pText)
		self.processes_text.type(DISABLED)
		self.resetLeftLabel()

	def setLeftLabel(self, s):
		self.left_label.config(text=("Current Process: "+s))
		self.root.update()

	def resetLeftLabel(self):
		self.left_label.config(text="Current Process: None")
		self.root.update()

	def getPassword(self):
		pwd = self.enc.decrypt()
		return pwd

	def getUserText(self):
		self.setLeftLabel("Getting Users...")
		u = Users()
		retstr = u.getUsers()
		ret = ''
		for i in retstr:
			ret += "User: " + i + "\n"
		self.resetLeftLabel()
		return ret

	def getGroupText(self):
		self.setLeftLabel("Getting Groups...")
		g = Groups()
		retstr = g.getGroups()
		ret = ''
		for i in retstr:
			ret += i + "\n"
		self.resetLeftLabel()
		return ret

	def getServicesText(self):
		self.setLeftLabel("Getting Services...")
		s = Services()
		retstr = s.getservicesbasic()
		self.resetLeftLabel()
		return retstr

	def getFirewallStatus(self):
		self.setLeftLabel("Getting Firewall Status...")
		f = Firewall()
		retstr = f.getStatus(self.enc.decrypt())
		self.resetLeftLabel()
		return retstr

	def getProcessesText(self):
		self.setLeftLabel("Getting Processes...")
		p = Processes()
		retstr = p.getprocesses()
		self.resetLeftLabel()
		return retstr

	def basicUpdate(self):
		if tkMessageBox.askyesno("SecureMe - Update", "Proceed with update?") == True:
			self.setLeftLabel("Updating Machine...")
			ud = Update()
			ud.update(self.enc)
			self.resetLeftLabel()
		else:
			pass

	def basicUpgrade(self):
		if tkMessageBox.askyesno("SecureMe - Upgrade", "Proceed with upgrade?") == True:
			self.setLeftLabel("Upgrading Machine...")
			ud = Update()
			ud.upgrade(self.enc)
			self.resetLeftLabel()
		else:
			pass

	def packageUpdate(self):
		if tkMessageBox.askyesno("SecureMe - Package Update", "Proceed with package update?") == True:
			self.setLeftLabel("Updating Packages...")
			ud = Update()
			ud.updateall(self.enc)
			self.resetLeftLabel()
		else:
			pass

	def enableFirewall(self):
		if tkMessageBox.askyesno("SecureMe - Firewall", "Are you sure you want to enable the firewall?") == True:
			self.setLeftLabel("Enabling Firewall...")
			f = Firewall()
			f.enable(self.getPassword())
			self.refresh("NONE")
			self.resetLeftLabel()
		else:
			pass

	def disableFirewall(self):
		if tkMessageBox.askyesno("SecureMe - Firewall", "Are you sure you want to disable the firewall?") == True:
			self.setLeftLabel("Disabling Firewall...")
			f = Firewall()
			f.disable(self.getPassword())
			self.refresh("NONE")
		else:
			pass

	def quitMenu(self):
		if tkMessageBox.askyesno("Secure Me - Quit?", "Are you sure you want to quit?") == True:
			sys.exit(0)
		else:
			pass