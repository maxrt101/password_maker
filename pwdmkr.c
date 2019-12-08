#include <time.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int i, n, x, r_chr;
char chr;
char *src;
int option;
int len = 16;
char * mode = NULL; 
char password[1024];

void gen_src(){
	if (mode) {
		if (!strcmp(mode, "l")) {
			src = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
		} else if (!strcmp(mode, "n")) {
			src = "0123456789";
		} else if (!strcmp(mode, "b")) {
			src = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
		} else {
			printf("Unknown mode: %s\n", mode);
			exit(0);
		}
	} else {
		mode = "b";
	}
}

void gen_pwd() {
	for (x = 0; x < strlen(password); x++) {
		password[n] = 0;
	}
	
	srand(time(NULL));
	int len_ = strlen(src);
	for (i = 0; i < len; i++) {
		r_chr = rand() % len_;
		chr = src[r_chr];
		password[i] = chr;
	}
	printf("%s\n", password);

}

void main(int argc, char *argv[]) {
	if (argc > 1) {
		for (i = 0; i < argc-1; i++) {
			while ((option = getopt(argc, argv, ":hvl:m:d:")) != -1) {
				switch (option) {
					case 'h': 
						printf("pwdmkr v0.1\nUsage: encrypt [-h] [-v] [-l LENGTH] [-m MODE]\n\nOptions:\n\t-h - Displays this help massage\n\t-v Displays version and exits\n\t-l - Length of password. Default 16\n\t-m - Mode. Can be l(letters), n(numbers) or b(both)\n");
						exit(0);
					case 'v':
						printf("pwdmkr v0.1 (c)2019 maxrt101\n");
						exit(0);
					case 'l':
						sscanf(optarg, "%d", &len);
						break;
					case 'm':
						mode = optarg;
						break;
					case  ':':
						printf("Option '-%c' needs an argument\n", option);
						exit(0);
					case '?':
						printf("Unknown argument\n");
						exit(0);
				}
			}
		}
	}
	gen_src();
	gen_pwd();
}
