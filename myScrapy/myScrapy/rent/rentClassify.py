# -- coding: utf-8 --
import re

from pandas import np
from sklearn.feature_extraction.text import TfidfVectorizer

from classify import assess
from myScrapy.mysql.MySqlUtils import MySqlUtil
from scipy.linalg import norm
import datetime

dbUtil = MySqlUtil()


def get_station(text):
    '''
    寻找文本中第一个出现的地铁站点名称,并且根据文本中出现的地铁站数量，预测创建者身份
    :param text:文本
    :return: 地铁站点,(1/0) 1:表示预测为广告贴，0不确定
    '''
    from myScrapy.rent import stations
    metro = dict()
    # 遍历地铁list，找到文本中地铁站点
    for station in stations.stations:
        if text.find(station) >= 0 and station not in metro:
            metro[station] = text.find(station)
    if len(metro) == 0:  # 如果没有出现过地铁站，返回空
        return None, 0
    # 按字典集合中，每一个元组的第二个元素排列。
    metro_order = sorted(metro.items(), key=lambda x: x[1], reverse=False)
    # 如果文本中第一次出现的站点为商圈站点，并且文本中所有的站点数小于等于3 则认为商圈附近的租房信息
    if metro_order[0][0] in stations.business_station and len(metro_order) <= 3:
        return metro_order[0][0], 0
    for k, v in metro_order:
        # 删除商圈的地铁站点
        if k in stations.business_station:
            metro.pop(k)
    if len(metro) > 3:
        # 同一个帖子中地铁站点大于三个，则帖子会认为广告贴。
        return metro_order[0][0], 1
    else:
        return metro_order[0][0], 0


def get_pay(text):
    """
    寻找文本中付款方式
    :param text:
    :return:
    """
    pay_way1 = r'押一付一|付一押一|押1付1|付1押1|月付|付一压一|压一付一'
    pay_way3 = r'押一付三|付三押一|押1付3|付3押1|季付|付三压一|压一付三'

    pay = None
    if re.search(pay_way1, text) is not None:
        pay = 1
    if re.search(pay_way3, text) is not None:
        pay = 3
    return pay


def get_only_girl(text):
    """
    寻找文本中是否仅限制女生合租
    :param text:
    :return:
    """
    # 仅限女生合租要求
    only_girl_word = r'限女生|女生合租|女生室友|室友是女生|全女生|限妹子|一个妹子|租女生|女生合住|只要女生|只租.｛0.4｝小姐姐|女室友'
    only_girl = None
    if re.search(only_girl_word, text) is not None:
        only_girl = 1
    return only_girl


def get_price(text):
    """
    提取文本中的价格相关信息
    :param text:
    :return:
    """
    price = None
    # 正则匹配，非数字字符+任意三个数字+0+非数字字符和路、弄、号、站、米等字符
    price_word = r'\D\d{3}0(\D|^[路弄号站米-])'
    match = re.search(price_word, text)
    if match:
        price = match.group(0)
        # 如果有符合要求的，根据长度提取出价格信息
        if len(price) == 5:
            price = price[1:]
        if len(price) == 6:
            price = price[1:-1]
        return price
    else:
        return price


def get_rent_type(text):
    """
    分类器分析文本的出租类型
    :param text:
    :return:
    """
    return classifier.predict(text)[0]


def get_creator_count(creator):
    """
    查询30天内creator发表的帖子数
    :param creator: 创建者id
    :return: 发表贴子数
    """
    today = datetime.date.today()
    # 30天前的时间
    date = today + datetime.timedelta(days=-30)
    sql = "select  count(*) from house_info where creator=(%s) and  crawDate>=(%s)"
    count = dbUtil.get_one(sql, [creator, date])
    return count[0]


def get_creator_count(creator):
    """
    查询30天内creator发表的帖子数
    :param creator: 创建者id
    :return: 发表贴子数
    """
    dbUtil = MySqlUtil()
    today = datetime.date.today()
    # 30天前的时间
    date = today + datetime.timedelta(days=-30)
    sql = "select  count(*) from house_info where creator=(%s) and  crawDate>=(%s)"
    count = dbUtil.get_one(sql, [creator, date])
    return count[0]


def analysis(url, creator, text):
    """
    分析文本中的各个信息
    :param url:  帖子链接
    :param creator: 创建者
    :param text: 标题+内容
    :return: 返回分类结果信息的列表
    """

    station, identity = get_station(text)
    pay = get_pay(text)
    price = get_price(text)
    only_girl = get_only_girl(text)
    rentType = get_rent_type(text)
    count = get_creator_count(creator)
    info = [url, station, identity, price, pay, only_girl, rentType, count, datetime.datetime.now()]
    return info


model_dir = '/root/hupiao/myScrapy/classify/models'  # 模型存放目录
data_dir = '/root/hupiao/myScrapy/classify/feature_space'  # 特征数据存放目录
classifier = assess.Logistic(data_dir, model_dir)


def getHouseInfo():
    for i in range(69):
        start = 1000 * i
        sql = "select * from  house_info_temp limit " + str(start) + ",1000"
        infos = dbUtil.get_all(sql)
        infoSaveSql = "insert into rent_info_temp (url, station, `identity`,price,pay,only_girl,rent_type,create_date) values (%s,%s,%s,%s,%s,%s,%s,%s)"
        # 保存信息分类
        for info in infos:
            res = analysis(info[5], info[6], info[1] + info[3])
            dbUtil.save(infoSaveSql, res)
            print(res)


def check(houses, title):
    if houses is None:
        return True
    else:
        for house in houses:
            if tfidf_similarity(house[0], title) > 0.65:
                return False
        return True


def tfidf_similarity(s1, s2):
    def add_space(s):
        return ' '.join(list(s))

    # 将字中间加入空格
    s1, s2 = add_space(s1), add_space(s2)
    # 转化为TF矩阵
    cv = TfidfVectorizer(tokenizer=lambda s: s.split())
    corpus = [s1, s2]
    vectors = cv.fit_transform(corpus).toarray()
    # 计算TF系数
    return np.dot(vectors[0], vectors[1]) / (norm(vectors[0]) * norm(vectors[1]))


if __name__ == '__main__':
    # url = "testurl"
    # creator = "textuser"
    # text1 = "标题：🌲6号线，金桥路地铁站，精装燃气一室户3300，16分钟直达世纪大道，可转乘2/4/9号线，交通方便，小区门口紧邻金桥国际，久金广场等"
    # text2 = "👠【地铁一号线】💋【无中介费】近中庚环创中心，1号线地铁站，东苑商务楼；女生合租、主卧➕独卫➕公用厨房；押一付一，给你舒适的居住体验哟！"
    # 分析文本  id   title  createDate  text  crawDate  url  creator
    getHouseInfo()
