#Designed by Luke Dinkler and Peter Toth 2015
import os, admin
from rootpassencryption import *

e = Encryption()
if os.path.exists("p.dat"):
	UserPasswd = e.decrypt()
else:
	print("Error: No password file loaded!")
	
class Ports():
	def showopen(self):
		portdata = os.popen("netstat -tulpn").read()
		return portdata
	
		
