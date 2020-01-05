// pwdmkr.js v1 by maxrt101

//genPwd(length, mode, delimiter, delimiter_length)
function genPwd() {
	length = 16;
	mode = 'b';
	delimiter = '-';
	delimiter_length = 4;
	var a = "";
	if (mode == 'l') {
		var src = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";	
	} else if (mode == 'n') {
		var src = "0123456789";
	} else if (mode == 'b') {
		var src = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
	} else {
		return "Error: mode is incorrect";
	}

	var i;
    var pwdsrc = "";
    values = new Uint32Array(length);
    window.crypto.getRandomValues(values);
    for(i=0; i<length; i++)
    {
        pwdsrc += src[values[i] % src.length];
    }
    source= pwdsrc.split(""); 

	var cnt = [];
	for (var i = 0; i <= (length - 1); i++) {
    	cnt.push(i);
	}

	for (i in cnt)
	{
		if ( (Number(i) + 1 ) % delimiter_length  == 0) {
			if ((Number(i) + 1 ) != length) {
				a += source[i] + delimiter;
			} else {
				a += source[i];	
			}
		} else {
			a += source[i];
		}
	}
	document.getElementById("pw").textContent = a;
}
document.getElementById('gen').onclick = genPwd;
