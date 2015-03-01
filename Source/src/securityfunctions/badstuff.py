#Created by Luke Dinkler and Peter Toth
import os, admin
from rootpassencrpytion import *

e = Encryption()
if os.path.exists("p.dat"):
	UserPasswd = e.decrypt()
else:
	print("No password file loaded!")

class Secure():
	def netcat(self):
		if os.path.exists("/bin/nc"):
			return False
		else:
			admin.AdminExec("apt-get purge netcat-openbsd")
			admin.AdminExec("apt-get purge netcat-traditional") #One may fail, that's alright!
			return True
		
	
			
