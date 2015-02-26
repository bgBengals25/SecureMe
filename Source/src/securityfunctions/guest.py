# Made by Luke Dinkler and Peter Toth
import admin, os
from rootpassencryption import *

enc = Encryption()
UserPasswd = enc.decrypt()

class GuestAccount():

	def enable(self):
		print('')

	def disable(self):
		print("Disabling Guest Account...")
		if os.path.exists("/usr/share/lightdm/lightdm.conf.d/50-ubuntu.conf"):
			admin.AdminExec('echo "allow-guest=false" >> /usr/share/lightdm/lightdm.conf.d/50-ubuntu.conf')
 
