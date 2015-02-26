# Made by Luke Dinkler and Peter Toth
import admin, os 
from rootpassencryption import *

enc = Encryption()
if os.path.exists("p.dat"):
	UserPasswd = enc.decrypt()

class Users():

	def __init__(self):
		print('')

	def deluser(self, user):
		admin.AdminExec("deluser -r " + user, UserPasswd)

	def adduser(self, username):
		admin.AdminExec('adduser ' + user + ' gecos -- " , , , ," --disabled-password', UserPasswd)
		





class Groups():

	def __init(self):
		print('')

	def adduser(self, user, group):
		admin.AdminExec( + group, UserPasswd)

