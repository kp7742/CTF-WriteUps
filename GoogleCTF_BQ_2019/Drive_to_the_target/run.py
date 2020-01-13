from collections import namedtuple
from bs4 import BeautifulSoup
from enum import Enum
import requests
import random
import pickle
import time
import os

CACHE_FILE = "cache.db"
URL = "https://drivetothetarget.web.ctfcompetition.com/"
Result = namedtuple('Result', 'lat lon token msg')

UNIT = 0.0001

class Message(Enum):
    CLOSER      = 1
    FURTHER     = 2
    TOO_FAST    = 3
    OTHER       = 4

def extract_info(html):
    parsed_html = BeautifulSoup(html, features="html.parser")
    lat = parsed_html.body.find("input", attrs={"name": "lat"})["value"]
    lon = parsed_html.body.find("input", attrs={"name": "lon"})["value"]
    token = parsed_html.body.find("input", attrs={"name": "token"})["value"]
    paragraphs = parsed_html.body.find_all("p")
    msg_type = Message.OTHER
    if len(paragraphs) > 1:
        msg = paragraphs[1].text
        if "closer" in msg:
            msg_type = Message.CLOSER
        elif "away" in msg:
            msg_type = Message.FURTHER
        elif "fast" in msg:
            msg_type = Message.TOO_FAST
        else:
            print (msg)

    return Result(lat, lon, token, msg_type)

def send_info(s, lat, lon, token):
    r = s.get(URL, params = {"lat": str(lat), "lon": str(lon), "token": token})
    return extract_info(r.text)

def get_direction(s, res, timeout, allow_diagonal = False):
    print ("Changing direction . . .")
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    random.shuffle(directions)

    if allow_diagonal:
        directions = [(-1, -1), (1, 1), (1, -1), (-1, 1)] + directions
    for direction in directions:
        while True:
            time.sleep(timeout)
            res = send_info(s, float(res.lat) + (UNIT * direction[0]), float(res.lon) + (UNIT * direction[1]), res.token)
            if res.msg == Message.CLOSER:
                print ("New direction: {}".format(direction))
                return res, direction
            elif res.msg == Message.TOO_FAST:
                timeout += 1
            else:
                break
    return (None, None)


s = requests.session()

if os.path.exists(CACHE_FILE):
    res = pickle.load( open( CACHE_FILE, "rb" ) )
else:
    r = s.get(URL)
    res = extract_info(r.text)
    
try:
    timeout = 0.8
    res, direction = get_direction(s, res, timeout, True)

    print ("Starting to drive . . .")

    while res is not None:
        time.sleep(timeout)

        res = send_info(s, float(res.lat) + (UNIT * direction[0]), float(res.lon) + (UNIT * direction[1]), res.token)
        print (res)
        if (res.msg == Message.FURTHER):
            res, direction = get_direction(s, res, timeout, False)
        elif (res.msg == Message.TOO_FAST):
            timeout += 0.1
        elif (res.msg == Message.OTHER):
            break

except Exception as e:
    print (e)
finally:
    pickle.dump( res, open( CACHE_FILE, "wb" ) )