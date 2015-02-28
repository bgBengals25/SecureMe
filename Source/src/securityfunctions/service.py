#Made by Peter Toth and Luke Dinkler
import os, admin
from rootpassencryption import *

p = Encryption()
if os.path.exists("p.dat"):
	UserPasswd = p.decrypt()
else:
	print("No password File loaded!")
	
class Services():
	def getservicesext(self):
		svcraw = os.system("ps aux | less >> services.txt")
		svcfile = open("services.txt", "r")
		services = svcfile.read().split("\n")

		return services

	def getservicesbasic(self):
		services = os.popen("service --status-all").read()
		#services = svcraw.split("\n ")
		return services
	
	def stop(self, service):
		admin.AdminExec("service " + service + " stop", UserPasswd)
		
	def start(self, service):
		admin.AdminExec("service " + service + " start", UserPasswd)
		
	
		
	        
	
	
		

