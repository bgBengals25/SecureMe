# Made by Luke Dinkler and Peter Toth
import os, subprocess

class Firewall():
	def enable(self):
		print('Enabling Universal Firewall...')
<<<<<<< HEAD
		subprocess.Popen(['/usr/bin/pkexec', "ufw enable"])
		print('Firewall Enabled!")
=======
		os.system("sudo ufw enable")
		print('Firewall Enabled!')
>>>>>>> c5de9d2b19f39708fec84ba24e50e937b2ab78ae

	def disable(self):
		print('Disabling Universal Firewall...')
		subprocess.Popen(['/usr/bin/pkexec', "ufw disable"])
		print('Firewall Disabled!')

	def addexception(self, exception):
		print('insert code here')


