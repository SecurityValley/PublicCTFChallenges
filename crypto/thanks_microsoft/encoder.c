#include <stdio.h>
#include <string.h>
#include <stdlib.h>

u_int32_t encodeChar(unsigned char *s) {

    u_int32_t result = 0;

    unsigned int ln = (int) s & 0x0F;
    unsigned int hn = (int) s >> 4 & 0x0F;

    u_int8_t x = 0;
    u_int8_t y = 0;

    if(hn <= 9) {
        x = 11;
    } else {
        x = 26;
    }

    if(ln <= 9) {
        y = 14;
    } else {
        y = 26;
    }

    if(hn > 9) {
        hn -= 9;
    }

    if(ln > 9) {
        ln -= 9;
    }


    result |= 0x0E;
    result = result << 6;

    result |= y;
    result = result << 4;

    result |= ln;
    result = result << 6;

    result |= x;
    result = result << 4;

    result |= hn;

    return result;
}

int main(int argc, char *argv[]) {

    if(argc != 2) {
        printf("please give one text input to encode \n");
        exit(0);
    }

    char *input = malloc(strlen(argv[1]));
    strcpy(input, argv[1]);

    for(int i = 0; i < strlen(input); i ++) {
        int chr = encodeChar(input[i]);
        printf("%x", chr);
    }

    printf("\n");
    free(input);

    return 0;
}

