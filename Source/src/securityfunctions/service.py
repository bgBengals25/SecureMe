#Made by Peter Toth and Luke Dinkler
import os, admin
from rootpassencryption import *

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
	
	
		
	        
	
	
		

