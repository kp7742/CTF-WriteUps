#include <stdio.h>
#include <string.h>

char* alphabet = "abcdefghijklmnopqrstuvwxyz";

char* unscramble(char* bytes, int bytesize, char* key, int keylen){
    int i = 0, j = 0;
    char* out = (char *) malloc(bytesize);
    for (i = 0; i < bytesize; ++i ){
        out[i] = bytes[i] ^ key[j++ % keylen];
    }
    return out;
}

unsigned char hexData[30] = {
    0x1F, 0x19, 0x0C, 0x1C, 0x30, 0x21, 0x2B, 0x14, 0x00, 0x06, 0x1D, 0x1A, 0x1B, 0x0A, 0x41, 0x16,
    0x00, 0x01, 0x5D, 0x01, 0x05, 0x0A, 0x5E, 0x09, 0x19, 0x1C, 0x07, 0x09, 0x1C, 0x0D 
};

int main()
{
    char *key = (char *) malloc(0x64u);
    key[3] = alphabet[18];
    key[5] = alphabet[20];
    key[0] = alphabet[14];
    key[4] = alphabet[18];
    key[2] = alphabet[14];
    key[1] = alphabet[15];
    key[6] = alphabet[12];
    printf("%s\n", key);
    
    char* s = strdup(key);
    int slen = strlen(s);

    char* result = unscramble(hexData, 30, s, slen);
    printf("%s\n", result);
    return 0;
}