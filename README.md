 # Python password maker(generator)

### Requirments:

 -Python =< 2.7  

Python modules:  
 -sys  
 -random  
 -string  
 -argparse  
 -functools  

### Usage examples:
 ./pwdmkr.py  
 ./pwdmkr.py -m l  
 ./pwdmkr.py -d - -dl 4  
 ./pwdmkr.py -l 32 -m l  
 ./pwdmkr.py -l 16 -m b -d - -dl 4  
 ./pwdmkr.py -l 32 -m b -d - -dl 8  
 ./pwdmkr.py -l 12 -m n -d '#' -dl 2  
 ./pwdmkr.py -l 1028 - m n -d . -dl 64  
 ./pwdmkr.py -l 12 -m n -d . -dl 3  
 ./pwdmkr.py -l 10000 | lolcat  
