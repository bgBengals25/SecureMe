# Made by Luke Dinkler and Peter Toth
# THIS FILE WILL BE USED FOR UPDATING THE MACHINE
import admin, os
from rootpassencryption import *

enc = Encryption()
if os.path.exists("p.dat"):
	UserPasswd = enc.decrypt()

class Update():

	def update(self):
		print("Just updating (nothing special)...")
		admin.AdminExec('apt-get update', UserPasswd)

	def update_upgrade(self):
		print("Upgrading new packages...")
		admin.AdminExec('apt-get upgrade', UserPasswd)


	def updateall(self):
		print("Completely upgrading all packages...")
		admin.AdminExec('apt-get dist-upgrade', UserPasswd)
