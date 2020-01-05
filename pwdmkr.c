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
int delimiter_len = 1;
char delimiter[16];
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
		gen_src();
	}
}


void gen_pwd() {
	srand(time(NULL));
	int len_ = strlen(src);

	if (strcmp(delimiter, "n")) {
		len = len + (len/delimiter_len);
		delimiter_len = delimiter_len + 1;

		for (i = 0; i < len; i++) {
			r_chr = rand() % len_;
			chr = src[r_chr];
			if (i % delimiter_len == 0) {
				password[i] = delimiter[0];
			} else {
				password[i] = chr;
			}
		}
		password[0] = ' ';
	} else {
		for (i = 0; i < len; i++) {
			r_chr = rand() % len_;
			chr = src[r_chr];
			password[i] = chr;
		}
	}

	printf("%s\n", password);	
}

void main(int argc, char *argv[]) {
	if (argc > 1) {
		for (i = 0; i < argc-1; i++) {
			while ((option = getopt(argc, argv, ":hvl:m:d:D:")) != -1) {
				switch (option) {
					case 'h': 
						printf("pwdmkr v0.22\nUsage: ./pwdmkr [-h] [-v] [-l LENGTH] [-m MODE]\n\nOptions:\n\t-h - Displays this help massage\n\t-v - Displays version and exits\n\t-l - Length of password. Default 16\n\t-m - Mode. Can be l(letters), n(numbers) or b(both)\n\t-d - Delimiter. Default - none\n\t-D - Delimiter length (interval)\n");
						exit(0);
					case 'v':
						printf("pwdmkr v0.22 (c)2020 maxrt101\n");
						exit(0);
					case 'l':
						sscanf(optarg, "%d", &len);
						break;
					case 'm':
						mode = optarg;
						break;
					case 'd':
						strcpy(delimiter, optarg);
						break;
					case 'D':
						delimiter_len = atoi(optarg);
						break;
					case  ':':
						printf("Option needs an argument!\n");
						exit(0);
					case '?':
						printf("Unknown option\n");
						exit(0);
				}
			}
		}
	}
	gen_src();
	gen_pwd();
}
