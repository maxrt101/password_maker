#pwdmkr v6.0b3 by maxrt101
import os
import sys
sys.dont_write_bytecode = True
import random
import string
import argparse
from functools import reduce

parser = argparse.ArgumentParser(description='''Python password maker. Example: python pwdmkr.py  -l 16  -m ln  -d -  -dl 4 ''')
parser.add_argument('-v', action='store_true', help='Display version and exit')
parser.add_argument('-s', action='store_true', help='Save password to file')
parser.add_argument('-fs', action='store_true', help='Force save password to file')
parser.add_argument('-f', action='store', dest='file', type=str,help='Destination file to save', default='password.txt')
parser.add_argument('-l', action='store', dest='length',type=int, help='Length of password', default=16)
parser.add_argument('-m', action='store', dest='mode', type=str, help='Mode: letters only(l), numbers only(n), symbols(s)(e.g. ln, s, ns, lns)', default='ln')
parser.add_argument('-d', action='store', dest='delimiter', help='Delimiter', default='')
parser.add_argument('-dl', action='store', dest='delimiter_len', type=int, help='Length between delimiters', default=0)
	
args = parser.parse_args()

version = '6.0b3'

config = {
	"len": 16,
	"mode": "both",
	"delimiter": "",
    "delimiter_len": 0,
    "source": []
}

config["len"] = args.length
config["mode"] = args.mode
config["delimiter"] = args.delimiter
config["delimiter_len"] = args.delimiter_len


def gen_src(source, max):
	a = ""
	for i in range(0, max):
		a += random.choice(source)
	return a

def main():
	if 'l' in list(config["mode"]):
		config["source"] += string.letters
	if 'n'  in list(config["mode"]):
		config["source"] += ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	if 's' in list(config["mode"]):
		config["source"] += ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '<', '>', '/', '?', '[', ']', '{', '}', '.', ',', '|', ':', ';']

	if config["source"] == []:
		print('ERROR: bad mode(-m)')
		exit()

	src = gen_src(config["source"], config["len"])
	pwd = reduce((lambda x, y: x + config["delimiter"] + y if ((len(x) + 1) % (config["delimiter_len"] + 1) == 0)  else x + y), list(src))
	print(pwd)

	if args.file == True and args.s != True or args.file == True and args.fs != True:
		print('''NOTE: -f won't work without -s or -fs''')

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
elif args.length > 250000:
	print('ERROR: Length > 250000, terminating')
	exit()
elif len(args.delimiter) > 100:
	print('ERROR: delimiter > 100, terminating')
	exit()
else: 
	main()