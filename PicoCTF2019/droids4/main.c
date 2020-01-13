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

unsigned char hexData[31] = {
    0x11, 0x05, 0x13, 0x07, 0x22, 0x36, 0x23, 0x0F, 0x1D, 0x00, 0x01, 0x5E, 0x11, 0x0D, 0x02, 0x1C,
    0x08, 0x01, 0x10, 0x18, 0x12, 0x1D, 0x19, 0x09, 0x4F, 0x1F, 0x19, 0x04, 0x0D, 0x1B, 0x18 
};

int main()
{
    char *key = "alphabetsoup";
    printf("%s\n", key);
    
    char* s = strdup(key);
    int slen = strlen(s);

    char* result = unscramble(hexData, 31, s, slen);
    printf("%s\n", result);
    return 0;
}