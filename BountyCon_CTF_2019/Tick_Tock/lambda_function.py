import base64
import json
import pickle
import time
import function_shield

function_shield.configure({
    "policy": {
        # 'block' mode => active blocking
        # 'alert' mode => log only
        # 'allow' mode => allowed, implicitly occurs if key does not exist
        "outbound_connectivity": "block",
        "read_write_tmp": "block",
        "create_child_process": "block",
        "read_handler": "block"
    },
    "token": "XXXXXXXX",
    "disable_analytics": "true"
})

def clock_page(past):
    html = '<!DOCTYPE HTML>'\
            + '<HTML>'\
            + '<HEAD>'\
            + '<TITLE>Timer</TITLE>'\
            + '<LINK rel="stylesheet" href="https://fonts.googleapis.com/css?family=Orbitron">'\
            + '<STYLE>'\
            + 'body{background: black;}'\
            + '.clock{position: absolute; top: 50%; left: 50%; transform: translateX(-50%) translateY(-50%); color: #17D4FE; font-size: 60px; font-family: Orbitron; letter-spacing: 7px;}'\
            + '</STYLE>'\
            + '</HEAD>'\
            + '<BODY>'\
            + '<DIV id="timer" class="clock" onload="showTime()"></DIV>'\
            + '<SCRIPT>'\
            + 'function showTime(){'\
            + 'var future = Date.now() / 1000 | 0;'\
            + 'var delta = future - ' + past + ';'\
            + 'var time = delta.toString();'\
            + 'document.getElementById("timer").innerText = time;'\
            + 'document.getElementById("timer").textContent = time;'\
            + 'setTimeout(showTime, 1000);'\
            + '}'\
            + 'showTime();'\
            + '</SCRIPT>'\
            + '</BODY>'\
            + '</HTML>'
    return html

class Epoch(object):
    def __init__(self, timestamp):
        self.ts = timestamp

flag = "BountyCon{[redacted]}"

def lambda_handler(event, context):
    if (('multiValueHeaders' in event.keys()) and (json.dumps(event['multiValueHeaders']) != 'null')):
        if ('cookie' not in event['multiValueHeaders'].keys()):
            url = event['requestContext']['path']
            epoch = Epoch('{:d}'.format(int(time.time())))
            cookie = base64.b64encode(pickle.dumps(epoch))
            return {
                'isBase64Encoded': 0,
                'statusCode': 302,
                'headers': {
                    'Content-Type': 'text/html; charset=utf-8',
                    'Set-Cookie': cookie, # Server time may be different to browser time!
                    'Location': url
                },
                'body': ''
            }
    epoch = pickle.loads(base64.b64decode(event['multiValueHeaders']['cookie'][0]))
    return {
        'isBase64Encoded': 0,
        'statusCode': 200,
        'headers': {'Content-Type': 'text/html; charset=utf-8'},
        'body': clock_page(epoch.ts)
    }
