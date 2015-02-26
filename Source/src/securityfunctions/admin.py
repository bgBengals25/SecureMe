#Made by Peter Toth and Luke Dinkler
import os

def AdminExec(command, passwd):
	cmd = "echo " + passwd + " | sudo -S " + command
	print(cmd)	
	os.system(cmd)

