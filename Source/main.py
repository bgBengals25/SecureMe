# Made by Luke Dinkler and Peter Toth

from src.gui.gui import InitGUI #Imports GUI module
from src.securityfunctions.rootpassencryption import Encryption

def start(): #Defines Start function
	enc = Encryption()
	gui = InitGUI(enc) #Initializes GUI
	print('Created GUI')

if __name__ == '__main__':
	start() #Starts the Software