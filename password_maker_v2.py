#test
import random
import string

l = {'letters', 'l'}
n = {'numbers', 'n'}
ln = {'both', 'b'}

class bcolors:
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'

b1 = None
b2 = None
b3 = None
b4 = None

a = None
choice = None


def func():
	global a
	if choice in l:
		a = random.choice(string.letters)
	elif choice in n:
		a = random.choice(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
	elif choice in ln:
		a = random.choice([random.choice(string.letters), random.choice(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])])
	else:
		print("error")		



def main():
	block1()
	block2()
	block3()
	block4()
	print("Here is your password")
	print(b1 + '-' + b2 + '-' + b3 + '-' + b4)


def block1():	
	func()
	l1 = a
	func()
	l2 = a
	func()
	l3 = a
	func()
	l4 = a
	global b1
	b1 = l1 + l2 + l3 + l4 

def block2():
	func()
	l5 = a
	func()
	l6 = a
	func()
	l7 = a
	func()
	l8 = a
	global b2
	b2 = l5 + l6+ l7 + l8 

def block3():
	func()
	l9 = a
	func()
	l10 = a
	func()
	l11 = a
	func()
	l12 = a
	global b3
	b3 = l9 + l10 + l11 + l12 

def block4():
	func()
	l13 = a
	func()
	l14 = a
	func()
	l15 = a
	func()
	l16 = a
	global b4
	b4 = l13 + l14 + l15 + l16 		


#ui
print(bcolors.BOLD + "PYTHON PASSWORD MAKER")
print(bcolors.ENDC + "What type of password you want to get: letters only, numbers only or both?(l/n/b)")

choice = raw_input()
main()

