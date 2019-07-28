#!/bin/bash
echo 'pwdmkr.py test v1'
a=pwdmkr_test.py

#python $a -h
python $a -v
echo ''
python $a
echo 'm: l'
python $a -m l
echo 'm: n'
python $a -m n
echo 'm: s'
python $a -m s
echo 'm: ln'
python $a -m ln
echo 'm: ls'
python $a -m ls
echo 'm: ns'
python $a -m ns
echo 'm: lns'
python $a -m lns
echo ' '

echo 'all test'
python $a -l 16 -m ln -d - -dl 4
python $a -l 20 -m lns -d '-' -d 4
echo ' '

echo 'save test'
echo '-f'
python $a -f file.txt
echo '-s -fs'
python $a -s -fs
echo '-s'
python $a -s
echo 'password.txt'
cat password.txt
echo $'\n' '-s 2t'
python $a -s
echo '-fs'
python $a -fs
echo 'password.txt'
cat password.txt
echo $'\n' 'rm password.txt'
rm password.txt
ls | grep password.txt
echo '-s -f'
python $a -s -f file.txt
echo 'file.txt'
cat file.txt
rm file.txt
echo ' '
