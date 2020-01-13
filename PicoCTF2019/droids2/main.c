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

unsigned char hexData[39] = {
    0x14, 0x00, 0x10, 0x02, 0x22, 0x27, 0x35, 0x55, 0x18, 0x0F, 0x06, 0x5A, 0x59, 0x0C, 0x12, 0x5A,
    0x11, 0x0A, 0x07, 0x05, 0x4F, 0x1E, 0x4F, 0x17, 0x0C, 0x1D, 0x1B, 0x07, 0x13, 0x4B, 0x40, 0x0A,
    0x1B, 0x18, 0x41, 0x12, 0x13, 0x0F, 0x6C 
};

int main()
{
    char *key = "dismass.ogg.weatherwax.aching.nitt.garlick";
    printf("%s\n", key);
    
    char* s = strdup(key);
    int slen = strlen(s);

    char* result = unscramble(hexData, 39, s, slen);
    printf("%s\n", result);
    return 0;
}