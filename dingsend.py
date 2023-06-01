import base64
import hashlib
import hmac
import time
from urllib.parse import quote_plus

import requests
import json
import datetime

import timestamp as timestamp


def send_msg(token_dd, secret, task, msg, pic):
    """
    通过钉钉机器人发送内容
    """
    timestamp = str(round(time.time() * 1000))
    url = 'https://oapi.dingtalk.com/robot/send?access_token=' + token_dd
    string_to_sign_enc = '{}\n{}'.format(timestamp, secret).encode('utf-8')
    hmac_code = hmac.new(secret.encode('utf-8'), string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = quote_plus(base64.b64encode(hmac_code))

    headers = {'Content-Type': 'application/json;charset=utf-8'}
    title_str = "定时任务推送：\n\n{0}\n".format(task)
    webhook = url + '&timestamp=' + timestamp + '&sign=' + sign
    data = {
        "msgtype": "feedCard",
        "feedCard": {
            "links": [{
                "title": title_str,
                "messageURL": "https://x2512239h2.goho.co/crontab",
                "picURL": pic
            }, {
                "title": msg,
                "messageURL": "https://x2512239h2.goho.co/crontab",
                "picURL": pic
            }
            ]
        }
    }

    res = requests.post(webhook, data=json.dumps(data), headers=headers)
    print(res.text)

    return res.text


def dingrobot(task, msg, pic, token_dd='6fb383a6fe26fddc1ae8336a63c4c332349a806c6fd3a6d919cd8f51ad05a311',
              secret='SEC74a210318ea12fa012ca622c17ae0b8ef2e9ffb3428e2b4133a50a432266ebe8'):
    send_msg(token_dd, secret, task, msg, pic)



