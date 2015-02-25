# Made by Luke Dinkler and Peter Toth

# This file encrypts and decrypts our code with our own encryption

class Encryption():

	FILE_LOCATION = 'p.dat'
	ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-_=+;:'`~.,/|"
	KEY =      "|Q7!A@Z1#W$'S%X3^E &8D*C4)R(F_V-T/G,5B.Y~H=9+N;6UJ:M1IK0OLP"

	def encrypt(self, passwd):
		file = open(self.FILE_LOCATION, 'w')
		original_list = list(passwd)
		alphabet_list = list(self.ALPHABET)
		key_list = list(self.KEY)
		encrypted_list = []

		for i in original_list:

			for a in alphabet_list:

				if i.lower() == a.lower():

					if i.istitle() == True:
						encrypted_list.append(key_list[alphabet_list.index(a)])
					elif i.istitle() == False:
						encrypted_list.append(key_list[alphabet_list.index(a)].lower())

		file.write("".join(encrypted_list))


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

		return "".join(decrypted_list)