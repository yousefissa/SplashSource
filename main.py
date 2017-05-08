import random
import requests
import selenium 
import time
import threading 
from dropconfig import *

# main menu
def menu():
	    print('''
Please read the readme on Github before using this bot.

This is a bot that allows you to do a few things: 

	1. Load proxies
	2. Get captcha balance.
    3. Quit. 
    ''')

	userChoice = input('Enter the action that you want to take: ')
	choices {
	1: load_proxies,
	2: captcha_balance,
	3: quit 
	}

	try:
		choices[int(userChoice)]()
	except:
        print('Input not recognized. You probably did not enter a number. \n'
              'The program will restart. \n')
        menu()
    finally:
        Continue()


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
