#pwdmkr v5 by maxrt101
import sys
sys.dont_write_bytecode = True
import random
import string
import argparse
from functools import reduce


parser = argparse.ArgumentParser(description='''Python password maker. Example: ./pwdmkr.py  -l 16  -m b  -d -  -dl 4 ''')
parser.add_argument('-v', action='store_true', help='Display version and exit')
parser.add_argument('-l', action='store', dest='length', help='Length of password', default=16)
parser.add_argument('-m', action='store', dest='mode', help='Mode: letters only(l), numbers only(n) or both(b)', default='b')
parser.add_argument('-d', action='store', dest='delimiter', help='Delimiter', default='')
parser.add_argument('-dl', action='store', dest='delimiter_len', help='Length between delimiters', default=0)

args = parser.parse_args()

version = '5'

config = {
	"len": 16,
	"mode": "both",
	"delimiter": "",
    "delimiter_len": 0,
    "source": []
}

config["len"] = int(args.length)
config["mode"] = args.mode
config["delimiter"] = args.delimiter
config["delimiter_len"] = int(args.delimiter_len)


def gen_pwd(source, max):
	a = ""
	for i in range(0, max):
		a += random.choice(source)
	return a


def main():
	if config["mode"] in ['l', 'letters', 'both', 'b']:
		config["source"] += string.letters
	if config["mode"] in ['n', 'nummbers', 'both', 'b']:
		config["source"] += ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 

	p = gen_pwd(config["source"], config["len"])
	p2 = reduce((lambda x, y: x + config["delimiter"] + y if ((len(x) + 1) % (config["delimiter_len"] + 1) == 0)  else x + y), list(p))
	print(p2)


if args.v == True:
	print('pwdmkr v{} (c)2019 maxrt101'.format(version))
else: 
	main()