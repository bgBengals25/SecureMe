# Made by Luke Dinkler and Peter Toth

# This file encrypts and decrypts our code with our own encryption

from Crypto import Random
from Crypto.Cipher import AES

class Encryption():

	FILE_LOCATION = 'p.dat'
	KEY = b'\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18'

	def pad(self, s):
		return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

	def enc(self, passwd):
		passwd = self.pad(passwd)
		iv = Random.new().read(AES.block_size)
		cipher = AES.new(self.KEY, AES.MODE_CBC, iv)
		return iv + cipher.encrypt(passwd)

	def dec(self, ciphertext):
		iv = ciphertext[:AES.block_size]
		cipher = AES.new(self.KEY, AES.MODE_CBC, iv)
		plaintext = cipher.decrypt(ciphertext[AES.block_size:])
		return plaintext.rstrip(b"\0")

	def encrypt(self, plaintext):
		enc = self.enc(plaintext)
		with open(self.FILE_LOCATION, 'wb') as f:
			f.write(enc)

	def decrypt(self):
		with open(self.FILE_LOCATION, 'rb') as f:
			ciphertext = f.read()
		dec = self.dec(ciphertext)
		return dec