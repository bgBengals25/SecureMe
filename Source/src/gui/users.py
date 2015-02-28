# Made by Luke Dinkler and Peter Toth

import Tkinter
from Tkinter import *
import tkMessageBox
import os
os.system("cd ..")
from src.securityfunctions.users import *
from src.securityfunctions.rootpassencryption import *
from src.securityfunctions.admin import *

class AddUser():

	def __init__(self):
		self.root = Tk()
		self.root.geometry("400x200+300+300")
		self.root.title("SecureMe - Add User")
		self.root.config()

		self.users = Users()
		self.enc = Encryption()

		mainlabel = Label(self.root, text="Add User - Enter Required Data Fields")
		mainlabel.pack()

		self.errorLabel = Label(self.root, text="")
		self.errorLabel.pack()

		fieldFrame = Frame(self.root)
		fieldFrame.pack()

		Label(fieldFrame, text="Username: ").grid(sticky=E)
		Label(fieldFrame, text="Password: ").grid(sticky=E)
		Label(fieldFrame, text="Password(repeat): ").grid(sticky=E)

		usernameVar = StringVar()
		passwordVar = StringVar()
		password2Var = StringVar()
		usernameEntry = Entry(fieldFrame, textvariable=usernameVar).grid(row=0, column=1)
		passwordEntry = Entry(fieldFrame, textvariable=passwordVar, show="*").grid(row=1, column=1)
		password2Entry = Entry(fieldFrame, textvariable=password2Var, show="*").grid(row=2, column=1)

		submit = Button(self.root, text="Submit", command=lambda : self.submit(usernameVar.get(), passwordVar.get(), password2Var.get()))
		submit.pack()

		self.root.mainloop()

	def submit(self, username, password, password2):

		print(username + " " + password + " " + password2)
		if password == password2:
			self.errorLabel.configure(text="")

			self.users.adduser(username)
			#admin.adminSetPassword(self.enc.decrypt(), username, password)

			self.root.destroy()

			tkMessageBox.showinfo("SecureMe - User Created", "Successfully Created User: '" + username + "'!")

		elif password != password2:
			self.errorLabel.configure(text="*Passwords do not match!")



class DelUser():

	def __init__(self, username):
		print('do nothing')