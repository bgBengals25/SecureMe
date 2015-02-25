# Made by Luke Dinkler and Peter Toth
import os, subprocess, admin


class Firewall():
	def enable(self):
		print('Enabling Universal Firewall...')

		admin.AdminExec("ufw enable")
		print('Firewall Enabled!")

	def disable(self):
		print('Disabling Universal Firewall...')
		admin.AdminExec("ufw disable")
		print('Firewall Disabled!')

	def addexception(self, exception):
		print('insert code here')


