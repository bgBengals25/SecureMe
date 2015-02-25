# Made by Luke Dinkler and Peter Toth

# This file encrypts and decrypts our code with our own encryption

import re

class Encryption():

	FILE_LOCATION = 'p.dat'
	ALPHABET = "abcdefghijklmnopqrstuvwkyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-_=+;:'`~.,/| "
	KEY =      "|oQ7!nA@pZm1#W$ql'S%rXk3^sE jt&8Diu*C4h)Rv(F_gV-Tw/fG,5xeB.Ydy~H=9cz+N;b6UJa:M1IK0`OLP"

	def encrypt(self, passwd):
		file = open(self.FILE_LOCATION, 'w')
		original_list = list(passwd)
		alphabet_list = list(self.ALPHABET)
		key_list = list(self.KEY)
		encrypted_list = []

		for i in original_list:

			for a in alphabet_list:

				if i.lower() == a.lower():
						encrypted_list.append(key_list[alphabet_list.index(a)])

		encrypted_string = ''
		for indx in encrypted_list:
			encrypted_string += str(indx)

		file.write(encrypted_string)


	def decrypt(self):
		file = open(self.FILE_LOCATION, 'r')
		encrypted_list = list(file.read())
		alphabet_list = list(self.ALPHABET)
		key_list = list(self.KEY)
		decrypted_list = []

		for i in encrypted_list:

			for k in key_list:

				if i.lower() == k.lower():

					if i.istitle() == True:
						decrypted_list.append(alphabet_list[key_list.index(k)])
					elif i.istitle() == False:
						decrypted_list.append(alphabet_list[key_list.index(k)].lower())

		decrypted_string = ''
		for indx in decrypted_list:
			decrypted_string += str(indx)

		return decrypted_string