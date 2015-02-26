# Made by Luke Dinkler and Peter Toth
# THIS FILE WILL BE USED FOR UPDATING THE MACHINE
import admin
from rootpassencryption import *

enc = Encryption()
UserPasswd = enc.decrypt()

class Update():

	def update(self):
		print("Just updating (nothing special)...")
		admin.AdminExec('apt get update', UserPasswd)

	def update_upgrade(self):
		print('')

	def updateall(self):
		print('')
		# this function also includes $ sudo apt-get dist-upgrade
