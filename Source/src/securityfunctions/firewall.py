# Made by Luke Dinkler and Peter Toth
import os, subprocess, admin
from rootpassencryption import *

class Firewall():
	def enable(self, rp):
		UserPasswd = rp
		print('Enabling Universal Firewall...')
		admin.AdminExec("ufw enable", UserPasswd)
		print('Firewall Enabled!')

	def disable(self, rp):
		UserPasswd = rp
		print('Disabling Universal Firewall...')
		admin.AdminExec("ufw disable", UserPasswd)
		print('Firewall Disabled!')

	def addexception(self, exception, rp):
		UserPasswd = rp
		print('insert code here')
