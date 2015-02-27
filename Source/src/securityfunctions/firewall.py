# Made by Luke Dinkler and Peter Toth
import os, subprocess, admin
from rootpassencryption import *
import tkMessageBox

class Firewall():
	def enable(self, rp):
		UserPasswd = rp
		print('Enabling Universal Firewall...')
		admin.AdminExec("ufw enable", UserPasswd)
		print('Firewall Enabled!')
		tkMessageBox.showinfo(title="SecureMe - Firewall", message="Successfully enabled the Firewall!")

	def disable(self, rp):
		UserPasswd = rp
		print('Disabling Universal Firewall...')
		admin.AdminExec("ufw disable", UserPasswd)
		print('Firewall Disabled!')
		tkMessageBox.showinfo(title="SecureMe - Updated", message="Successfully disabled the Firewall!")

	def getStatus(self, rp):
		UserPassword = rp
		print('Getting Status')
		status = os.popen(admin.getAdminExec("ufw status", UserPassword)).read()
		return status

	def addexception(self, exception, rp):
		UserPasswd = rp
		print('insert code here')
