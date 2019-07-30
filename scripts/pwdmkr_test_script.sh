#!/bin/bash

white='\033[0m'
green='\033[92m'
red='\033[91m'
blink='\033[5m'

if [ $1 = '-v' ]
then
	echo 'pwdmkr test v2b1 SH by maxrt101'
	exit
elif [ ${#1} -gt 4 ]
then 
	a=$1
else 
	a=pwdmkr.py
fi

stdbuf -oL python $a -v |
	while IFS= read -r line
	do
		echo "$line"
		if [ ${#line} -eq 28 ]
		then
			echo -e 'v           '$white'['$green'OK'$white']' 
		else
			echo -e 'v         '$white'['$red'FAIL'$white']'
		fi	
	done

echo $'\nmodes:'

stdbuf -oL python $a |
	while IFS= read -r line
	do
		echo "$line"
		if [ ${#line} -eq 16 ]
		then
			echo -e '            '$white'['$green'OK'$white']' 
		else
			echo -e '          '$white'['$red'FAIL'$white']'
		fi	
	done

stdbuf -oL python $a -m l |
	while IFS= read -r line
	do
		echo "$line"
		if [ ${#line} -eq 16 ]
		then
			echo -e 'm:l         '$white'['$green'OK'$white']' 
		else
			echo -e 'm:l       '$white'['$red'FAIL'$white']'
		fi	
	done

stdbuf -oL python $a -m n |
	while IFS= read -r line
	do
		echo "$line"
		if [ ${#line} -eq 16 ]
		then
			echo -e 'm:n         '$white'['$green'OK'$white']' 
		else
			echo -e 'm:n       '$white'['$red'FAIL'$white']'
		fi	
	done

stdbuf -oL python $a -m s |
	while IFS= read -r line
	do
		echo "$line"
		if [ ${#line} -eq 16 ]
		then
			echo -e 'm:s         '$white'['$green'OK'$white']' 
		else
			echo -e 'm:s       '$white'['$red'FAIL'$white']'
		fi	
	done

stdbuf -oL python $a -m ln |
	while IFS= read -r line
	do
		echo "$line"
		if [ ${#line} -eq 16 ]
		then
			echo -e 'm:ln        '$white'['$green'OK'$white']' 
		else
			echo -e 'm:ln      '$white'['$red'FAIL'$white']'
		fi	
	done

stdbuf -oL python $a -m ls |
	while IFS= read -r line
	do
		echo "$line"
		if [ ${#line} -eq 16 ]
		then
			echo -e 'm:ls        '$white'['$green'OK'$white']' 
		else
			echo -e 'm:ls      '$white'['$red'FAIL'$white']'
		fi	
	done

stdbuf -oL python $a -m ns |
	while IFS= read -r line
	do
		echo "$line"
		if [ ${#line} -eq 16 ]
		then
			echo -e 'm:ns        '$white'['$green'OK'$white']' 
		else
			echo -e 'm:ns      '$white'['$red'FAIL'$white']'
		fi	
	done

stdbuf -oL python $a -m lns |
	while IFS= read -r line
	do
		echo "$line"
		if [ ${#line} -eq 16 ]
		then
			echo -e 'm:lns       '$white'['$green'OK'$white']' 
		else
			echo -e 'm:lns     '$white'['$red'FAIL'$white']'
		fi	
	done


echo $'\ncombined test:'

stdbuf -oL python $a -l 16 -m ln -d - -dl 4 |
	while IFS= read -r line
	do
		echo "$line"
		if [ ${#line} -eq 19 ]
		then
			echo -e 'cmb         '$white'['$green'OK'$white']' 
		else
			echo -e 'cmb       '$white'['$red'FAIL'$white']'
		fi	
	done

stdbuf -oL python $a -l 20 -m lns -d '-' -d 4 |
	while IFS= read -r line
	do
		echo "$line"
		if [ ${#line} -eq 39 ]
		then
			echo -e 'cmb         '$white'['$green'OK'$white']' 
		else
			echo -e 'cmb       '$white'['$red'FAIL'$white']'
		fi	
	done


echo $'\nsave test:'

stdbuf -oL python $a -s |
	while IFS= read -r line
	do
		password_file=$(<password.txt)
		echo $"$line"
		if [ "$line" == "$password_file" ]
		then
			echo -e 's           '$white'['$green'OK'$white']' 
		else
			echo -e 's         '$white'['$red'FAIL'$white']'
		fi	
	done

stdbuf -oL python $a -fs |
	while IFS= read -r line
	do
		password_file=$(<password.txt)
		echo $'\n'"$line"
		if [ "$line" == "$password_file" ]
		then
			echo -e 'fs          '$white'['$green'OK'$white']' 
		else
			echo -e 'fs        '$white'['$red'FAIL'$white']'
		fi	
	done

rm password.txt
check_file_1= ls | grep password.txt
if [ ${#check_file_1} -eq 0 ]
then
	echo -e 'rm          '$white'['$green'OK'$white']' 
else
	echo -e 'rm        '$white'['$red'FAIL'$white']'
fi

stdbuf -oL python $a -s -f file.txt |
	while IFS= read -r line
	do
		password_file=$(<file.txt)
		echo $'\n'"$line"
		if [ "$line" == "$password_file" ]
		then
			echo -e 's f         '$white'['$green'OK'$white']' 
		else
			echo -e 's f       '$white'['$red'FAIL'$white']'
		fi	
	done

rm file.txt
check_file_2=$(ls | grep file.txt)
if [ ${#check_file_2} -eq 0 ]
then
	echo -e 'rm          '$white'['$green'OK'$white']' 
else
	echo -e 'rm        '$white'['$red'FAIL'$white']'
fi


echo $'\nerrors:'


stdbuf -oL python $a -s -fs |
	while IFS= read -r line
	do
		echo $line
		if [ ${#line} -eq 50 ]
		then
			if [ ${#line} -eq 50 ]
			then
				echo -e 's fs        '$white'['$green'OK'$white']' 
			else
				echo -e 's fs      '$white'['$red'FAIL'$white']'
			fi
		fi	
	done

echo $'\n'

touch password.txt
check_file_3=$(ls | grep password.txt)
if [ "$check_file_3" == "password.txt" ]
then
	echo -e 'touch       '$white'['$green'OK'$white']' 
else
	echo -e 'touch     '$white'['$red'FAIL'$white']'
fi

stdbuf -oL python $a -s |
	while IFS= read -r line
	do
		echo $line
		if [ ${#line} -eq 39 ]
		then
			if [ ${#line} -eq 39 ]
			then
				echo -e 's 2         '$white'['$green'OK'$white']' 
			else
				echo -e 's 2       '$white'['$red'FAIL'$white']'
			fi
		fi
	done

rm password.txt
check_file_4= ls | grep password.txt
echo $check_file_4
if [ ${#check_file_4} -eq 0 ]
then
	echo -e 'rm          '$white'['$green'OK'$white']' 
else
	echo -e 'rm        '$white'['$red'FAIL'$white']'
fi


stdbuf -oL python $a -l 250001 |
	while IFS= read -r line
	do
		echo "$line"
		if [ ${#line} -eq 38 ]
		then
			if [ ${#line} -eq 38 ]
			then
				echo -e 'l           '$white'['$green'OK'$white']' 
			else
				echo -e 'l         '$white'['$red'FAIL'$white']'
			fi	
		fi
	done

stdbuf -oL python $a -d '                                                                                                     ' |
	while IFS= read -r line
	do
		echo "$line"
		if [ ${#line} -eq 38 ]
		then
			if [ ${#line} -eq 38 ]
			then
				echo -e 'd           '$white'['$green'OK'$white']' 
			else
				echo -e 'd         '$white'['$red'FAIL'$white']'
			fi	
		fi
	done
