#Designed by Luke Dinkler and Peter Toth
import os, admin
from rootpassencryption import *
p = Encryption()
if os.path.exists("p.dat"):
	UserPasswd = p.decrypt()
else:
	print("No password file loaded!")

class Processes():
	
	def getprocesses(self):
		os.system("echo top >> processes.txt")
		pfile = open("processes.txt", 'r')
		processes = pfile.read()
		pfile.close()
		return processes

		
