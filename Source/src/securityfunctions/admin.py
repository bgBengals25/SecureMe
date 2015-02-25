#Made by Peter Toth and Luke Dinkler
import os

def AdminExec(command, passwd):
	cmd = "'echo %s|sudo -S %s' % (" + passwd + ", " + command + ")"
	os.system(cmd)

