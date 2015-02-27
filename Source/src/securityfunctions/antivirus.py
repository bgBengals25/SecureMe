#Designed by Luke Dinkler and Peter Toth
import os, admin
from rootpassencryption import *

p = Encryption()
if os.path.exists("p.dat"):
	UserPasswd = p.decrypt()
else:
	print("No password file loaded!")

class AntiVirus():
	def check(self):
		if os.path.exists("/bin/clamav"):
			return True
		else:
			return False 
	
	def install(self):
		admin.AdminExec("apt-get install clamav", UserPasswd)
	
		
		
			
		
