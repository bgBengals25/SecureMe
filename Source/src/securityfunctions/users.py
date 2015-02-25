# Made by Luke Dinkler and Peter Toth
import admin, os 
from rootpassencryption import *

UserPassword = encryption.decrypt()

class Users():

	def __init__(self):
		print('')

	def deluser(self, user):
		admin.AdminExec("userdel -r " + user, UserPassword)
		





class Groups():

	def __init(self):
		print('')
