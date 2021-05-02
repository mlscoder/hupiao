import json
import time
import requests
from bs4 import BeautifulSoup

def getStation(line):
    """
    :param line: 上海地铁线路号
    :return:线路的站点名称list
    """
    url = "http://m.shmetro.com/interface/metromap/metromap.aspx?func=lineStations&line=" + line

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    }

    response = requests.get(url, headers=headers)
    # 使用BeautifulSoup对象解析html
    soup = BeautifulSoup(response.text, 'html.parser')
    jsonObject = json.loads(soup.text)
    locations = jsonObject['levels'][0]['locations']
    locationList = []
    for location in locations:
        locationList.append(location['title'])
    return locationList


if __name__ == '__main__':
    # 地铁线路号
    lines = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '15', '16', '18', '41']
    allLocationList = []  # 存放所有的站点名称的列表
    for line in lines:
        locationList = getStation(line)
        allLocationList.extend(locationList)  # 每条线路的站点名称存放到主列表中
        time.sleep(1)  # 线程休眠1秒
    print(set(allLocationList))  # set去重
    print(len(set(allLocationList)))
