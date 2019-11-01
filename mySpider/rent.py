import re
import datetime

from mySpider.baiduapi import getHz
from mySpider.mysql.mysql_DBUtils import MyPymysqlPool
from mySpider.subway import stationList
from mySpider.plot import plot
import string


class rent:
    def __init__(self, hid, address, price, line, station, count, landlord, pay, renttype, createDate, onlygril):
        self.hid = hid
        self.address = address
        self.price = price
        self.line = line
        self.station = station
        self.landlord = landlord
        self.pay = pay
        self.count = count
        self.renttype = renttype
        self.createDate = createDate
        self.onlygril = onlygril


'''
hid 房子信息
title 标题
creator 创建者
text 租房信息的内容
'''


def anay(hid, title, creator, text):
    qiuzu = r'求租|求组|找房|求合租'
    if re.search(qiuzu, title) != None:
        return None

    allword = title + text
    # 地铁站要求
    ditie = r'\d{1,2}号线|M\d{1,2}|m{1,2}'
    num = r'\d{1,2}'
    # 判断是否包含支付方式
    payway1 = r'押一付一|付一押一|押1付1|付1押1|月付|付一压一|压一付一'
    payway3 = r'押一付三|付三押一|押1付3|付3押1'
    type1 = r'合租'
    type2 = r'整租'
    # 仅限女生合租要求
    onlygrilword = r'限女生|女生合租|女生室友|室友是女生|全女生|限妹子|一个妹子|租女生|女生合住|只要女生|只租.｛0.4｝小姐姐'

    # 判断是否包含价格
    price = r'\D\d{4}\D|\D\d{4}\s?$'
    quchu = r'路|弄|号|站|-|米'

    select = 0
    newprice = None
    matchp = re.search(price, allword)

    if matchp:
        newprice = matchp.group(0)
        # 如果不包含这些字符继续，否则的话pass
        if re.search(quchu, newprice) == None:
            if len(newprice) == 5:
                newprice = newprice[1:]
                select = select + 1
            if len(newprice) == 6:
                newprice = newprice[1:-1]
                select = select + 1
        else:
            newprice = None
    # 如果关键词中出现合租做标记，其他的pass/
    renttype = None

    if re.search(type1, allword) != None:
        renttype = 1
        select = select + 1
    if re.search(type2, allword) != None:
        renttype = 2
        select = select + 1

    if renttype==None:
        gettype = getHz(allword)
        if gettype == 'he':
            renttype = 1
        if gettype == 'zheng':
            renttype = 2

    # 寻找是否标注支付方式
    pay = None
    if re.search(payway1, allword) != None or re.search(payway1, allword) != None:
        pay = "1"
        select = select + 1
    if re.search(payway3, allword) != None or re.search(payway3, allword) != None:
        pay = "3"
        select = select + 1
    line = None
    if re.search(ditie, title) != None:
        line = re.search(num, re.search(ditie, title).group(0)).group(0)
        # 如果title中含有地铁线路，那么提取出几号线。
        select = select + 1
    station = None
    for one in stationList:
        if index_of_str(one, title) != None:
            station = one
            select = select + 1
            break

    '''
    查询当前创建者的id在当前一个月库中创建了几次。
    正常情况下，次数为6次以下，身份可能为二房东，或者只是出租一次的一房东 大于6次。可能是职业房东
    '''
    count = creatorcount(creator)
    landlord = None
    if count > 6:
        landlord = 2
    else:
        landlord = 1

    # 查找文字信息中时候含有小区名字的信息
    address = None
    for p in plot:
        if index_of_str(p, title + text) != None:
            address = p
            select = select + 1
    createDate = datetime.datetime.now()

    # 查找文字中是否仅限女生的要求
    onlygril = None
    if re.search(onlygrilword, allword) != None:
        onlygril = 1
        select = select + 1
    r1 = rent(hid, address, newprice, line, station, count, landlord, pay, renttype, createDate, onlygril)
    if select > 1:
        return r1
    else:
        return None


# 参数s1为源字符串，参数s2为要查找的字符串
# 查找title是否包含地铁站名

def index_of_str(s1, s2):
    if s2.find(s1) >= 0:
        return s1
    else:
        return None


# 统计一个月内创建者发布的条数
def creatorcount(creator):
    sql = "select count(*) from houseinfo where creator=(%s) and crawDate > DATE_SUB(NOW(),INTERVAL 1 MONTH) ;"
    mysql = MyPymysqlPool("dbMysql")
    count = mysql.getAll(sql, creator)
    return count[0]['count(*)']
