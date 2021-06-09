# -- coding: utf-8 --

# 查询同一个创建者最近一个月发布的帖子
from myScrapy.mysql.MySqlUtils import MySqlUtil
from myScrapy.rent import rentClassify


def haveOne(title):
    dbUtil = MySqlUtil()
    querySql = "select title from house_info where creator=(%s)  and crawDate >= DATE_SUB(NOW(),INTERVAL 30 day) "
    haveOne = ['204344844']
    houses = dbUtil.get_all(querySql, haveOne)
    for house in houses:
        if rentClassify.tfidf_similarity(house[0], title) > 0.8:
            return False
    return True


if __name__ == '__main__':
    print(haveOne(""))
