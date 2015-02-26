# Made by Luke Dinkler and Peter Toth

from src.gui.gui import InitGUI #Imports GUI module
from src.securityfunctions import admin, firewall, users, guest

def start(): #Defines Start function
	gui = InitGUI() #Initializes GUI
	print('Created GUI')

if __name__ == '__main__':
	start() #Starts the Software
