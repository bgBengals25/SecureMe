# Made by Luke Dinkler and Peter Toth

# This file encrypts and decrypts our code with our own encryption

class Encryption():

	FILE_LOCATION = 'p.dat'
	ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-_=+;:'`~.,/"
	KEY =      "Q7!A@Z1#W$'S%X3^E &8D*C4)R(F_V-T/G,5B.Y~H=9+N;6UJ:M1IK0OLP"

	def encrypt(self, passwd):
		file = open(self.FILE_LOCATION, 'w')
		encrypted_list = list(passwd)
		alphabet_list = list(self.ALPHABET)
		key_list = list(self.KEY)

		for i in encrypted_list:

			for a in alphabet_list:

				if i.lower() == a.lower():

					if i.istitle() == True:
						i = key_list[alphabet_list.index(a)]
					elif i.istitle() == False:
						i = key_list[alphabet_list.index(a)].lower()

		print(encrypted_list)


	def decrypt(self):
		print('')