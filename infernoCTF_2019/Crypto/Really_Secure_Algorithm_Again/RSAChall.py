import gmpy2
import string
 
e = 65537
N = 25693197123978473
enc_flag = ['0x2135d36aa0c278', '0x3e8f43212dafd7', '0x7a240c1672358', '0x37677cfb281b26', '0x26f90fe5a4bed0', '0xb0e1c482daf4', '0x59c069723a4e4b', '0x8cec977d4159']

p = 150758089
q = 170426657

def rsa_decrypt(p, q, e, c):
    n = p * q
    ph = (p - 1) * (q - 1)
    d = gmpy2.invert(e, ph)
    plaintext = pow(c, d, n)
    return int(plaintext)
	
flag = ''
for code in enc_flag:
	flag = flag + hex(rsa_decrypt(p,q,e,int(code, 16))).replace('0x','').decode("hex")

print(flag)	