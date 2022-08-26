import json

import requests as req

corpid = 'ww441664d5b785bbdb'  # 企业微信的 corpid
corpsecret = 'u9ry2P1Yhj0_F_LFjD3kgsKw4vat16TNqgUtQiMKfus'  # 企业微信 corpsecret
appid = '1000003'  # 企业微信 appid

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

send_wx('哈哈哈')