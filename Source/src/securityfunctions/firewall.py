# Made by Luke Dinkler and Peter Toth
import os, subprocess, admin

pwdfile = open("p.dat", "r") #Loads proposed password file
UserPasswd = pwdfile.read() #Gets Password from the file
pwdfile.close() #closes the file

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