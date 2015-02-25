# Made by Luke Dinkler and Peter Toth

class Firewall():
	def enable(self):
		print('Enabling Universal Firewall...')
		os.system("sudo ufw enable")
		print('Firewall Enabled!")

	def disable(self):
		print('Disabling Universal Firewall...')
		os.system("sudo ufw disable")
		print('Firewall Disabled!')

	def addexception(self, exception):
		print('insert code here')


