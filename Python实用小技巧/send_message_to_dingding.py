import json
import requests


def sendmessage(message):
    url = 'https://oapi.dingtalk.com/robot/send?access_token=bafdfc958a4f5320ec0ebe65f30843e51ef622596cf070c748280f58655e0051'  # 钉钉机器人的webhook地址
    HEADERS = {
        "Content-Type": "application/json ;charset=utf-8 "
    }
    message = message
    String_textMsg = {
        "msgtype": "text",
        "text": {"content": message},
        "at": {
            "atMobiles": [
                "17865563709"  # 如果需要@某人，这里写他的手机号
            ],
            "isAtAll": 0  # 如果需要@所有人，这些写1
        }
    }
    String_textMsg = json.dumps(String_textMsg)
    res = requests.post(url, data=String_textMsg, headers=HEADERS)
    print(res.text)


if '__name__' == '__main__':
    sendmessage()