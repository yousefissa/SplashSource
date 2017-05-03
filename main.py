import random
import requests
import selenium 
import time
import threading 
from dropconfig import *

# displays 2captcha balance
def captcha_balance(api_token):
	if api_token == '':
		print('No captcha token present. Check your config file.')
	else:
		balance = requests.get("http://2captcha.com/res.php?key={}&action=getbalance".format(api_token)).text
		print('Your 2captcha balance is, ', balance)

# imports proxies
try:
	with open('proxies.txt') as proxiesFile:
		proxies = proxiesFile.read().splitlines()
except IOError:
	print('Error importing proxy file.')
	exit()
