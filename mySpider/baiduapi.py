import json
import requests


def getHz(text):
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=9dqxI7aXbKkz8ufwdMlGMBp2&client_secret=kOMrO1z4ZMUM1ndOENwo8TVTsCCqqSvT'
    header = {'Content-Type': 'application/json; charset=UTF-8'}
    request = requests.get(host, header)
    Json = {"text": text}
    params = json.dumps(Json)
    request_url = 'https://aip.baidubce.com/rpc/2.0/ai_custom/v1/text_cls/hztype'
    access_token = json.loads(request.text)['access_token']
    request_url = request_url + "?access_token=" + access_token
    headers = {'Content-Type': 'application/json;charset=UTF-8'}
    response = requests.post(url=request_url, headers=headers, data=params.encode())
    if response.status_code == 200:
        if (json.loads(response.text)['results'][0]['score'] > 0.5):
            return json.loads(response.text)['results'][0]['name']
        if (json.loads(response.text)['results'][1]['score'] > 0.5):
            return json.loads(response.text)['results'][1]['name']
    return None


if __name__ == '__main__':
    text = "个人转租，没有中介费，朝南大阳台卧室1850，喜欢打我电话，微信同号"
    type = getHz(text)
    print(type)
