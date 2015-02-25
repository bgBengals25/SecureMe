# Made by Luke Dinkler and Peter Toth
import os, subprocess

class Firewall():
	def enable(self):
		print('Enabling Universal Firewall...')
		subprocess.Popen(['/usr/bin/pkexec', "ufw enable"])
		print('Firewall Enabled!')
		os.system("sudo ufw enable")
		print('Firewall Enabled!')

	def disable(self):
		print('Disabling Universal Firewall...')
		subprocess.Popen(['/usr/bin/pkexec', "ufw disable"])
		print('Firewall Disabled!')

	def addexception(self, exception):
		print('insert code here')