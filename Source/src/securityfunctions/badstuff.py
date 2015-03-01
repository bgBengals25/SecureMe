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
			admin.AdminExec("apt-get purge netcat-openbsd -y")
			admin.AdminExec("apt-get purge netcat-traditional -y") #One may fail, that's alright!	
			admin.AdminExec("apt-get purge netcat -y")
		else:
			return False
	def telnet(self):
		if os.path.exists("/usr/bin/telnet"):
			admin.AdminExec("apt-get purge telnet -y")
		else:
			return False
			
			
	
		
	
			
