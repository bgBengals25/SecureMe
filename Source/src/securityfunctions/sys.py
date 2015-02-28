#Designed by Luke Dinkler and Peter Toth
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
		
	
