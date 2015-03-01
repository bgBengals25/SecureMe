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
	
	def killportprocess(self, port):
		a = os.popen(admin.getAdminExec("lsof -i :" + port + " -t", UserPasswd)).read()
		print(a)
		if a == None:
			return "Port is not in use"
		else:
			os.system("kill " + a)
	
	def getportprocess(self, port):
		pid = os.popen(admin.getAdminExec("lsof -i :" + port + " -t", UserPasswd)).read()
		print(pid)
		if pid == None or pid == " " or pid == "\n" or pid == "":
			return "Port is not in use"
		else:
			b = os.popen("ps -p " + pid + " -o comm=").read()
			return b
			
			
		
		
		
	
		
