import random
import string
from functools import reduce


config = {
	"len": 16,
	"mode": "both"
}

choice = None
a = None
length = 5

def gen_pwd(source, max):
	a = ""
	for i in range(0, max):
		a += random.choice(source)
	return a

"""
def gen_pwd(source, max):
	a = ""
	for i in range(0, max): 
		a += random.choice(source)
	return a
"""

def get_config():
	print("Choose Lenght of your password(defualt 16): ")
	length = raw_input()
	if length != "":
		config["len"] = int(length)
	print("What type of password you want to get: letters only, numbers only or both?(l/n/b) (default both)")
	choice = raw_input()
	if choice != '':
		config["mode"] = choice
	config["source"] = []
	if config["mode"] in ['l', 'letters', 'both', 'b']:
		config["source"] += string.letters
	if config["mode"] in ['n', 'nummbers', 'both', 'b']:
		config["source"] += ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 


print("PYTHON PASSWORD MAKER")

#print("Do you want to choose lenght of your password")
#yn = raw_input()
#if yn in y :	
#	if lenght == 16 :
#		print("What kind of delimiter you want to use?")
#		delimiter = raw_input()


get_config()

p = gen_pwd(config["source"], config["len"])
print("Here is your password {}".format(p))

p2 = reduce((lambda x, y: x + "-" + y if ((len(x) + 1) % (5 + 1) == 0)  else x + y), list(p))
print("Here is your password {}".format(p2))
