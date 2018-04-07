import random
import string

l = {'letters', 'l'}
n = {'numbers', 'n'}
ln = {'both', 'b'}

class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

b1 = None
b2 = None
b3 = None
b4 = None


#letters + numbers
def both():
	block1()
	block2()
	block3()
	block4()
	print("Here is your password")
	print(b1 + '-' + b2 + '-' + b3 + '-' + b4)


def block1():	
	l1 = random.choice([random.choice(string.letters), random.choice(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])])
	l2 = random.choice([random.choice(string.letters), random.choice(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])])
	l3 = random.choice([random.choice(string.letters), random.choice(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])])
	l4 = random.choice([random.choice(string.letters), random.choice(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])])
	global b1
	b1 = l1 + l2 + l3 + l4 

def block2():
	l5 = random.choice([random.choice(string.letters), random.choice(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])])
	l6 = random.choice([random.choice(string.letters), random.choice(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])])
	l7 = random.choice([random.choice(string.letters), random.choice(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])])
	l8 = random.choice([random.choice(string.letters), random.choice(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])])
	global b2
	b2 = l5 + l6+ l7 + l8 

def block3():
	l9 = random.choice([random.choice(string.letters), random.choice(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])])
	l10 = random.choice([random.choice(string.letters), random.choice(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])])
	l11 = random.choice([random.choice(string.letters), random.choice(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])])
	l12 = random.choice([random.choice(string.letters), random.choice(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])])
	global b3
	b3 = l9 + l10 + l11 + l12 

def block4():
	l13 = random.choice([random.choice(string.letters), random.choice(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])])
	l14 = random.choice([random.choice(string.letters), random.choice(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])])
	l15 = random.choice([random.choice(string.letters), random.choice(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])])
	l16 = random.choice([random.choice(string.letters), random.choice(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])])
	global b4
	b4 = l13 + l14 + l15 + l16 		
#end


#numbers
def num():
	def main_n():
		block1()
		block2()
		block3()
		block4()
		print("Here is your password")
		print(b1 + '-' + b2 + '-' + b3 + '-' + b4)


	def block1():		
		l1 = random.choice(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
		l2 = random.choice(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
		l3 = random.choice(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
		l4 = random.choice(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
		global b1
		b1 = l1 + l2 + l3 + l4 

	def block2():
		l5 = random.choice(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
		l6 = random.choice(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
		l7 = random.choice(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
		l8 = random.choice(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
		global b2
		b2 = l5 + l6+ l7 + l8 

	def block3():
		l9 = random.choice(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
		l10 = random.choice(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
		l11 = random.choice(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
		l12 = random.choice(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
		global b3
		b3 = l9 + l10 + l11 + l12 

	def block4():
		l13 = random.choice(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
		l14 = random.choice(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
		l15 = random.choice(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
		l16 = random.choice(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
		global b4
		b4 = l13 + l14 + l15 + l16 	

	main_n()	
#end


#letters
def let():
	def main_l():
		block1()
		block2()
		block3()
		block4()
		print("Here is your password")
		print(b1 + '-' + b2 + '-' + b3 + '-' + b4)


	def block1():	
		l1 = random.choice(string.letters)
		l2 = random.choice(string.letters)
		l3 = random.choice(string.letters)
		l4 = random.choice(string.letters)
		global b1
		b1 = l1 + l2 + l3 + l4 

	def block2():
		l5 = random.choice(string.letters)
		l6 = random.choice(string.letters)
		l7 = random.choice(string.letters)
		l8 = random.choice(string.letters)
		global b2
		b2 = l5 + l6+ l7 + l8 

	def block3():
		l9 = random.choice(string.letters)
		l10 = random.choice(string.letters)
		l11 = random.choice(string.letters)
		l12 = random.choice(string.letters)
		global b3
		b3 = l9 + l10 + l11 + l12 

	def block4():
		l13 = random.choice(string.letters)
		l14 = random.choice(string.letters)
		l15 = random.choice(string.letters)
		l16 = random.choice(string.letters)
		global b4
		b4 = l13 + l14 + l15 + l16 
	main_l()			
#end



#ui
print(bcolors.BOLD + "PYTHON PASSWORD MAKER")
print(bcolors.ENDC + "What type of password you want to get: letters only, numbers only or both?(l/n/b)")

choice = raw_input()

if choice in l:
	let()
elif choice in n:
	num()
elif choice in ln:
	both()
else:
	sys.stdout.write(bcolors.FAIL + "Please respond with l, n or b")
	print bcolors.ENDC + ""	


#l = random.choice(string.letters)
#n = random.choice(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
#a = random.choice([random.choice(string.letters), random.choice(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])])
#print(bcolors.ENDC + b1 + b2 + b3 + b4)

