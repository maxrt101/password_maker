#pwdmkr v4
import sys
sys.dont_write_bytecode = True
import random
import string
from functools import reduce


config = {
	"len": 16,
	"mode": "both",
	"delimiter": "",
    "delimiter_len": 0
}

choice = None
a = None
length = 5


def gen_pwd(source, max):
	a = ""
	for i in range(0, max):
		a += random.choice(source)
	return a


def cmd():
	print("PYTHON PASSWORD MAKER")
	#get_config
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

	print("Choose delimiter: ")
	delimiter = raw_input()

	if delimiter != '':
		config["delimiter"] = delimiter
	
	print("Choose delimiter length: ")
	delimiter_len = raw_input()

	if delimiter_len != '':
		config["delimiter_len"] = int(delimiter_len)


	#gen_pwd
	p = gen_pwd(config["source"], config["len"])

	p2 = reduce((lambda x, y: x + config["delimiter"] + y if ((len(x) + 1) % (config["delimiter_len"] + 1) == 0)  else x + y), list(p))
	print("Here is your password {}".format(p2))

cmd()