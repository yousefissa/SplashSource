import random
import requests
import selenium 
import time
import threading 

# imports proxies
try:
	with open('proxies.txt') as proxiesFile:
		proxies = proxiesFile.read().splitlines()
except IOError:
	print('Error importing proxy file.')
	exit()


