import json
import os
import requests as req

corpid = os.environ["CORPID"]  # 企业微信的 corpid
corpsecret = os.environ["CORPSECRER"]  # 企业微信 corpsecret
appid = os.environ["APPID"]  # 企业微信 appid

def send_wx(x):
    url = f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}'
    r = req.get(url, timeout=5)
    tokens = json.loads(r.text)['access_token']
    url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=" + tokens
    data = {
        "touser": "@all",
        "msgtype": "text",
        "agentid": appid,
        "text": {
            "content": x
        },
        "safe": 0,
    }
    data = json.dumps(data)
    return req.post(url, data=data, timeout=9).text

print(send_wx('哈哈哈'))
