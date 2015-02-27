#Designed by Luke Dinkler and Peter Toth
import os, admin, commands
from rootpassencryption import *
p = Encryption()
if os.path.exists("p.dat"):
	UserPasswd = p.decrypt()
else:
	print("No password file loaded!")

class Processes():
	
	def getprocesses(self):
		'''pfile = os.popen("top -p 1 -n 1", "r")
		processes = pfile.read()
		pfile.close()'''
		output = commands.getoutput('top -b -n 1')
		return output

		
