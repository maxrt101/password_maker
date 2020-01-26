# Password maker(generator)

## Python password maker
### Installation:
1.[Download](https://github.com/maxrt101/password_maker/archive/master.zip) or [clone](https://github.com/maxrt101/password_maker) password maker.  
2.Make sure you have **python 3** and theese installed:  
 - os  
 - sys  
 - random  
 - string  
 - argparse  
 - functools  

3.Run (See usage)  

### Usage:
`python pwdmkr.py [-h] [-v] [-s] [-fs] [-f FILE] [-l LENGTH] [-m MODE] [-d DELIMITER] [-dl DELIMITER_LEN]`   

**Note**: You can't use -s and -fs at the same time

### Arguments:
**-h** - Help. Display help message and exit  
**-v** - Version. Display version and exit  
**-s** - Save password into file  
**-fs** - Force save file  
**-f** - File name. Default password.txt  

**-l** - Length. Lenght of password (without delimiters). Default 16  
**-m** - Mode. Mode of generating password: l - letters, n - numbers, s - symbols, c - custom(can be combined to form `ls` or `ln` or `sn`). Default `ln`  
**-d** - Delimiter. Default none  
**-dl** - Delimiter length. Default 0
  
**--unrestricted** - Unrestricted mode. Surpasses any restrictions, like delimiter length, and overall length  
  

## JS password maker  
### Installation:  
If you want to use `pwdmkr.js` in your html page, you must include it in `<head>`:  
`<script src="/path/to/script/pwdmkr.js"></script>` (path relatively to `index.php` (or `index.html`, or whatever name you are using))  
  
### Usage (within `<script>`):  
`genPwd(length, mode, delimiter, delimiter_length)`  
  
### Where arguments are:  
**length** - Lenght of password (without delimiters). Default 16  
**mode** - Mode of generating password: l - letters, n - numbers, b - both. Default `b`  
**delimiter** - Default none  
**delimiter_length** - Default 0  

## C password maker  
### Installation:
1.[Download](https://github.com/maxrt101/password_maker/archive/master.zip) or [clone](https://github.com/maxrt101/password_maker) password maker.  
2.Run `gcc -o pwdmkr pwdmkr.c`  

### Usage:
`./pwdmkr [-h] [-v] [-l LENGTH] [-m MODE]`  

### Arguments:  
**-h** - Help. Display help message and exit  
**-v** - Version. Display version and exit  
**-l** - Length. Lenght of password (without delimiters). Default 16  
**-m** - Mode. Mode of generating password: l - letters, n - numbers, b - both. Default b  
**-d** - Delimiter. Default none  
**-D** - Delimiter length. Default 1  

## Chrome extension  
### Installation:
In order to install pwdmkr chrome extension, you must go to `chrome://extensions/`, enable developer mode and click on 'Load unpacked' then choose chrome_extension folder. That's it.  

### Usage:
Click on white square with 4 asterisks(\*), labeled 'Password Maker' and press 'Generate password' button  
