from decimal import *
 
e = 3
ciphertext = 2205316413931134031074603746928247799030155221252519872649613686408884798530321139183194114380675760980675288213509494488928149890378350358245536745970253162283534968545300178396900226131454240625540026296473434895830304509610598192929125

c = Decimal(ciphertext)

def find_invpow(x,n):
    """Finds the integer component of the n'th root of x,
    an integer such that y ** n <= x < (y + 1) ** n.
    """
    high = 1
    while high ** n <= x:
        high *= 2
    low = high/2
    while low < high:
        mid = (low + high) // 2
        if low < mid and mid**n < x:
            low = mid
        elif high > mid and mid**n > x:
            high = mid
        else:
            return mid
    return mid + 1

plain = find_invpow(c, e)

print(hex(int(Decimal(plain))))
