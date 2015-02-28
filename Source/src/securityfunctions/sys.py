#Designed by Luke Dinkler and Peter Toth 2015

import os, subprocess, admin
from rootpassencryption import *

e = Encryption()
if os.path.exists("p.dat"):
	UserPasswd = e.decrypt()
else:
	print("No password file loaded!")
	
class Linux():
	def shutdown(self, time):
		admin.AdminExec("shutdown -h " + time, UserPasswd)
	def reboot(self):
		admin.AdminExec("reboot", UserPasswd)
	def delete(self, filetorm):
		admin.AdminExec("rm " + filetorm, UserPasswd)
	def copy(self, source, destination):
		admin.AdminExec("cp " + source + " " + destination, UserPasswd)
	def systemsettings(self):
		if os.path.exists("/usr/bin/unity-control-center"):
			os.system("/usr/bin/unity-control-center")
		else:
			return False
	
	
