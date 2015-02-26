#Made by Peter Toth and Luke Dinkler
import os, admin
from rootpassencryption import *

class Services():
	def getservices(self):
		svcraw = os.popen("service --status-all").read()
		services = svcraw.split("\n")
		return services


