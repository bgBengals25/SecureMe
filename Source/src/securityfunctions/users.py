# Made by Luke Dinkler and Peter Toth
import admin, os, pwd
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
		
	def getusers(self):
		for i in range(1000, 2000):

        	try:
                	p = pwd.getpwuid(i)
                	return p[0]
        	except:
                	pass
		




class Groups():

	def __init(self):
		print('')

	def addtogroup(self, user, group):
		admin.AdminExec('usermod -a -G ' + group + ' ' + user, UserPasswd)

	def addtogroups(self, user, groups): #Here 'groups' is a list
		admin.AdminExec('usermod -a -G ' + str(groups) + ' ' + user, UserPasswd)


