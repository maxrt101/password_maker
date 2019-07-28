#pwdmkr pytester v1.1
import os
import sys 
sys.dont_write_bytecode = True
import argparse
from subprocess import call as system_call
from subprocess import check_output as check_output

parser = argparse.ArgumentParser(description='Pwdmkr tester')
parser.add_argument('-v', action='store_true', help='Display version and exit')
parser.add_argument('-s', action='store_true', help='Save test log to file')
parser.add_argument('-f', action='store', dest='file', type=str,help='Destination file to save', default='pwdmkr_test_log.txt')
parser.add_argument('-n', action='store', dest='name',type=str, help='Name of tested file', default='pwdmkr.py')
	
args = parser.parse_args()

class colors:
	WHITE = '\033[0m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
#	HEADER = '\033[95m'
#	BOLD = '\033[1m'
#	UNDERLINE = '\033[4m'

test_type = 'PY'
version = '1.1'

c_fail = colors.WHITE + '[' + colors.FAIL + 'FAIL' + colors.WHITE + ']'
c_ok = colors.WHITE + '[' + colors.OKGREEN + 'OK' + colors.WHITE + ']'

test_d = ' ' * 101

def main(name):
	system_call(['python', name, '-v'])
	if len(check_output(['python', name, '-v'])) <= 32:
		print('v' + ' ' * 11  + c_ok)
	else:
		print('v' + ' ' * 9  + c_fail)

	print('\nmodes:')

	system_call(['python', name])
	if len(check_output(['python', name])) == 17:
		print(' ' * 12  +  c_ok)
	else:
		print(' ' * 10  + c_fail)

	system_call(['python', name, '-m', 'l'])
	if len(check_output(['python', name, '-m', 'l'])) == 17:
		print('m:l' + ' ' * 9  + c_ok)
	else:
		print('m:l' + ' ' * 7  + c_fail)

	system_call(['python', name, '-m', 'n'])
	if len(check_output(['python', name, '-m', 'n'])) == 17:
		print('m:n' + ' ' * 9  + c_ok)
	else:
		print('m:n' + ' ' * 7  + c_fail)

	system_call(['python', name, '-m', 's'])
	if len(check_output(['python', name, '-m', 's'])) == 17:
		print('m:s' + ' ' * 9  + c_ok)
	else:
		print('m:s' + ' ' * 9  + c_fail)

	system_call(['python', name, '-m', 'ln'])
	if len(check_output(['python', name, '-m', 'ln'])) == 17:
		print('m:ln' + ' ' * 8  + c_ok)
	else:
		print('m:ln' + ' ' * 6  + c_fail)

	system_call(['python', name, '-m', 'ls'])
	if len(check_output(['python', name, '-m', 'ls'])) == 17:
		print('m:ls' + ' ' * 8  + c_ok)
	else:
		print('m:ls' + ' ' * 6  + c_fail)

	system_call(['python', name, '-m', 'ns'])
	if len(check_output(['python', name, '-m', 'ns'])) == 17:
		print('m:sn' + ' ' * 8  + c_ok)
	else:
		print('m:ns' + ' ' * 6  + c_fail)

	system_call(['python', name, '-m', 'lns'])
	if len(check_output(['python', name, '-m', 'lns'])) == 17:
		print('m:lns' + ' ' * 7  + c_ok)
	else:
		print('m:lns' + ' ' * 5  + c_fail)

	'''
	echo 'all test'
	python name -l 16 -m ln -d - -dl 4
	python name -l 20 -m lns -d '-' -d 4
	echo ' '
	'''
	
	print('\nsave test:')

	#system_call(['python', name, '-s'])
	test_s = check_output(['python', name, '-s'])[:16]
	print(test_s)
	if test_s == open('password.txt').read()[:16]:
		print('s' + ' ' * 11  + c_ok)
	else:
		print('s' + ' ' * 9  + c_fail)

	#system_call(['python', name, '-fs'])
	#if check_output(['python', name, '-fs'])[:16] == open('password.txt').read()[:16]:
	test_s = check_output(['python', name, '-fs'])[:16]
	print(test_s)
	if test_s == open('password.txt').read()[:16]:
		print('fs' + ' ' * 10  + c_ok)
	else:
		print('fs' + ' ' * 8  + c_fail)

	#system_call(['python',  name, '-s', '-f', 'file.txt'])
	#if check_output(['python',  name, '-s', '-f', 'file.txt'])[:16] == open('file.txt').read()[:16]:
	test_s = check_output(['python',  name, '-s', '-f', 'file.txt'])[:16]
	print(test_s)
	if test_s == open('file.txt').read()[:16]:
		print('s f' + ' ' * 9  + c_ok)
	else:
		print('s f' + ' ' * 7  + c_fail)


	system_call(['rm', 'password.txt'])
	if os.path.isfile('password.txt') == False:
		print('rm' + ' ' * 10  + c_ok)
	else:
		print('rm' + ' ' * 8  + c_fail)

	system_call(['rm', 'file.txt'])
	if os.path.isfile('password.txt') == False:
		print('rm' + ' ' * 10  + c_ok)
	else:
		print('rm' + ' ' * 8  + c_fail)


	print('\nerrors:')

	system_call(['touch', 'password.txt'])
	system_call(['python', name, '-s'])
	if len(check_output(['python', name, '-s'])) == 57:
		print('s' + ' ' * 11  + c_ok)
	else:
		print('s' + ' ' * 9  + c_fail)

	system_call(['rm', 'password.txt'])

	system_call(['python', name, '-s', '-fs'])
	if len(check_output(['python', name, '-s', '-fs'])) == 68:
		print('s fs' + ' ' * 8  + c_ok)
	else:
		print('s fs' + ' ' * 6  + c_fail)

	system_call(['python', name, '-l', '250001'])
	if len(check_output(['python', name, '-l', '250001'])) == 36:      #FROM 6.3 - 39
		print('l' + ' ' * 11  + c_ok)
	else:
		print('l' + ' ' * 9  + c_fail)

	system_call(['python', name, '-d', test_d])
	if len(check_output(['python', name, '-d', test_d])) == 36:        #FROM 6.3 - 39
		print('d' + ' ' * 11  + c_ok)
	else:
		print('d' + ' ' * 9  + c_fail)


if args.v:
	print('pwdmkr test v{} {} by maxrt101'.format(version, test_type))
else:
	main(args.name)
