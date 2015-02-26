# Made by Luke Dinkler and Peter Toth
# THIS FILE WILL BE USED FOR UPDATING THE MACHINE
import admin, os
import tkMessageBox

class Update():

	def __init__(self):
		print('init updater')

	def update(self, enc):
		UserPasswd = enc.decrypt()
		print("Just updating...")
		admin.AdminExec('apt-get update', UserPasswd)
		tkMessageBox.showinfo(title="SecureMe - Updated", message="Successfully Updated the system!")

	def update_upgrade(self, enc):
		UserPasswd = enc.decrypt()
		print("Upgrading new packages...")
		admin.AdminExec('apt-get upgrade', UserPasswd)
		tkMessageBox.showinfo(title="SecureMe - Updated", message="Successfully Upgraded the system!")

	def updateall(self, enc):
		UserPasswd = enc.decrypt()
		print("Completely upgrading all packages...")
		admin.AdminExec('apt-get dist-upgrade', UserPasswd)
		tkMessageBox.showinfo(title="SecureMe - Updated", message="Successfully Updated the packages on your system!")