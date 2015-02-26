# Made by Luke Dinkler and Peter Toth
import os, subprocess, admin
from rootpassencryption import *

enc = Encryption()
if os.path.exists("p.dat"):
	UserPasswd = enc.decrypt()

class Firewall():
	def enable(self):
		print('Enabling Universal Firewall...')

		admin.AdminExec("ufw enable", UserPasswd)
		print('Firewall Enabled!')

	def disable(self):
		print('Disabling Universal Firewall...')
		admin.AdminExec("ufw disable", UserPasswd)
		print('Firewall Disabled!')

	def addexception(self, exception):
		print('insert code here')
