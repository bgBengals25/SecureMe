#Made by Peter Toth and Luke Dinkler 2015
import os

def AdminExec(command, passwd):
	cmd = "echo " + passwd + " | sudo -S " + command #Combines sudo command withe the required password
	print(cmd)	
	os.system(cmd) #Executes it

def getAdminExec(command, passwd):
	cmd = "echo " + passwd + " | sudo -S " + command #Combines sudo command withe the required password
	print(cmd)
	return cmd

def adminpopen(command, passwd):
	cmd = "echo " + passwd + " | sudo -S " + command
	os.popen("echo " + passwd + " | sudo -S " + command).read()
