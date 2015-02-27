#Designed by Luke Dinkler and Peter Toth
import os, admin
from rootpassencryption import *
p = Encryption()
if os.path.exists("p.dat"):
	p.decrypt()
else:
	print("No password file loaded!")

class Processes():
	
	def getprocesses(self):
		processes = os.popen("top").read()
		return processes


		
