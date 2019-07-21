# Python password maker(generator)

### Installation:
1.[Download](https://github.com/maxrt101/python_password_maker/archive/master.zip) or [clone](https://github.com/maxrt101/python_password_maker) python password maker.  
2.Make sure you have **python 2.7** and theese installed:  
 - os  
 - sys  
 - random  
 - string  
 - argparse  
 - functools  

3.Run (See usage)  

### Usage:
`python pwdmkr.txt [-h] [-v] [-s] [-fs] [-f FILE] [-l LENGTH] [-m MODE] [-d DELIMITER] [-dl DELIMITER_LEN]` or  
`./pwdmkr.txt [-h] [-v] [-s] [-fs] [-f FILE] [-l LENGTH] [-m MODE] [-d DELIMITER] [-dl DELIMITER_LEN]`  

**Note**: You can't use -s and -fs in the same time

### Arguments:
**-h** - Help. Display help message and exit  
**-v** - Version. Display version and exit  
**-s** - Save password into file  
**-fs** - Force save file  
**-f** - File name. Default password.txt  

**-l** - Length. Lenght of password (without delimiters). Default 16  
**-m** - Mode. Mode of generating password: l - letters, - n - numbers, b - both. Default b  
**-d** - Delimiter. Default none  
**-dl** - Delimiter length. Default 0


### Usage examples:
 `./pwdmkr.py`  
 `./pwdmkr.py -m l`  
 `./pwdmkr.py -d - -dl 4`  
 `./pwdmkr.py -l 32 -m l`  
 `./pwdmkr.py -l 16 -m b -d - -dl 4`  
 `./pwdmkr.py -l 32 -m b -d - -dl 8`  
 `./pwdmkr.py -l 12 -m n -d '#' -dl 2`  
 `./pwdmkr.py -l 1028 - m n -d . -dl 64`  
 `./pwdmkr.py -l 12 -m n -d . -dl 3`  
 `./pwdmkr.py -l 10000 | lolcat`  
