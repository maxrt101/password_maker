#pwdmkr v5.3 by maxrt101
import os
import sys
sys.dont_write_bytecode = True
import random
import string
import argparse
from functools import reduce


parser = argparse.ArgumentParser(description='''Python password maker. Example: ./pwdmkr.py  -l 16  -m b  -d -  -dl 4 ''')
parser.add_argument('-v', action='store_true', help='Display version and exit')
parser.add_argument('-s', action='store_true', help='Save password to file')
parser.add_argument('-fs', action='store_true', help='Force save password to file')
parser.add_argument('-f', action='store', dest='file', help='Destination file to save', default='password.txt')
parser.add_argument('-l', action='store', dest='length', help='Length of password', default=16)
parser.add_argument('-m', action='store', dest='mode', help='Mode: letters only(l), numbers only(n) or both(b)', default='b')
parser.add_argument('-d', action='store', dest='delimiter', help='Delimiter', default='')
parser.add_argument('-dl', action='store', dest='delimiter_len', help='Length between delimiters', default=0)


args = parser.parse_args()

version = '5.3'

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


def gen_src(source, max):
	a = ""
	for i in range(0, max):
		a += random.choice(source)
	return a


def main():
	if config["mode"] in ['l', 'letters', 'both', 'b']:
		config["source"] += string.letters
	if config["mode"] in ['n', 'nummbers', 'both', 'b']:
		config["source"] += ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 

	src = gen_src(config["source"], config["len"])
	pwd = reduce((lambda x, y: x + config["delimiter"] + y if ((len(x) + 1) % (config["delimiter_len"] + 1) == 0)  else x + y), list(src))
	print(pwd)

	if args.s and args.fs:
		print('''ERROR: Arguments -s and -fs can't be used together''')
	else:	
		if args.s or args.fs:
			if os.path.isfile(args.file) and args.s:
				print('ERROR: File {} already exists'.format(args.file))
			else:
				pwdfile = open(args.file, 'w')
				pwdfile.write(pwd)
				pwdfile.close()



if args.v:
	print('pwdmkr v{} (c)2019 maxrt101'.format(version))
else: 
	main()