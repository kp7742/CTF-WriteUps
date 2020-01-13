#include <stdio.h>
#include <string.h>

char* unscramble(char* bytes, int bytesize, char* key, int keylen){
    int i = 0, j = 0;
    char* out = (char *) malloc(bytesize);
    for (i = 0; i < bytesize; ++i ){
        out[i] = bytes[i] ^ key[j++ % keylen];
    }
    return out;
}

unsigned char hexData[26] = {
    0x11, 0x0E, 0x02, 0x06, 0x2D, 0x39, 0x2F, 0x08, 0x07, 0x00, 0x1D, 0x49, 0x03, 0x12, 0x15, 0x47,
    0x0F, 0x43, 0x1A, 0x10, 0x01, 0x08, 0x1A, 0x04, 0x09, 0x1A 
};

int main()
{
    char *key = "againmissing";
    printf("%s\n", key);
    
    char* s = strdup(key);
    int slen = strlen(s);

    char* result = unscramble(hexData, 26, s, slen);
    printf("%s\n", result);
    return 0;
}