from pwn import *

host = '2019shell1.picoctf.com'
port = int(22)
user = 'NullVoid'
password = 'a1b2c3d4'
remote_path = '/problems/time-s-up_2_af1f9d8c14e16bcbe591af8b63f7e286/times-up'

shell = ssh(user, host, port, password)
shell.set_working_directory(symlink=True)

py = shell.run(remote_path)
py.recvuntil('Challenge: ')

expr = py.recvline()
result = os.popen('(equation="' + expr + '"; /bin/echo ${equation}) | bc').read()
py.sendline('122')

print('\nExpression: ' + expr)
print('\nResult: ' + result)

print('\nFlag: ' + py.recvline())