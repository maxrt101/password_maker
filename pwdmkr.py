#pwdmkr v5b1
import sys
sys.dont_write_bytecode = True
import random
import string
import argparse
from functools import reduce

#args
parser = argparse.ArgumentParser(description='Python password maker')
parser.add_argument('-v', action='store_true', help='Display version and exit')
parser.add_argument('-l', action='store', dest='length', help='Length of password', default=16)
parser.add_argument('-m', action='store', dest='mode', help='Mode: letters only(l), numbers only(n) or both(b)', default='b')
parser.add_argument('-d', action='store', dest='delimiter', help='Delimiter', default='')
parser.add_argument('-dl', action='store', dest='delimiter_len', help='Length between delimiters', default=0)

args = parser.parse_args()
#print(args.accumulate(args.integers))

version = '5b1'


config = {
	"len": 16,
	"mode": "both",
	"delimiter": "",
   "delimiter_len": 0,
   "source": []
}

#write_config
config["len"] = int(args.length)
config["mode"] = args.mode
config["delimiter"] = args.delimiter
config["delimiter_len"] = int(args.delimiter_len)

#choice = None
#a = None
#length = 5


def gen_pwd(source, max):
	a = ""
	for i in range(0, max):
		a += random.choice(source)
	return a


def main():
	print("PYTHON PASSWORD MAKER")
	#get_config_old
#	print("Choose Lenght of your password(defualt 16): ")
#	length = raw_input()
#	if length != "":
#		config["len"] = int(length)
	
#	print("What type of password you want to get: letters only, numbers only or both?(l/n/b) (default both)")
#	choice = raw_input()

#	config["source"] = []

	if config["mode"] in ['l', 'letters', 'both', 'b']:
		config["source"] += string.letters
	if config["mode"] in ['n', 'nummbers', 'both', 'b']:
		config["source"] += ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 

#	print("Choose delimiter: ")
#	delimiter = raw_input()

#	if delimiter != '':
#		config["delimiter"] = delimiter
	
#	print("Choose delimiter length: ")
#	delimiter_len = raw_input()

#	if delimiter_len != '':
#		config["delimiter_len"] = int(delimiter_len)


	#gen_pwd
	p = gen_pwd(config["source"], config["len"])

	p2 = reduce((lambda x, y: x + config["delimiter"] + y if ((len(x) + 1) % (config["delimiter_len"] + 1) == 0)  else x + y), list(p))
	print("Here is your password {}".format(p2))

if args.v == True:
	print('pwdmkr v{} (c)2019 maxrt101'.format(version))
else: 
	main()
