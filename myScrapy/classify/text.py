# -- coding: utf-8 --
import os

from myScrapy.mysql.MySqlUtils import MySqlUtil

dbUtils = MySqlUtil()


def getZz():
    """
    查询整租数据
    :return:
    """
    sql = "SELECT title ,text  FROM houseinfo where crawDate >='2021-01-01' and (title like '%整租%' or  text like  '%整租%' ) and title  not like '%合租%'  and  text not like '%合租%'  "
    datas = dbUtils.get_all(sql)
    # 检查目录是否存在，不存在则创建
    zzdir = "text/zz/"
    if not os.path.exists(zzdir):
        os.mkdir(zzdir)
    for i in range(2000):
        with open(zzdir + "/z" + str(i) + ".txt", "w", encoding="utf-8") as file:
            file.write(datas[i][0] + datas[i][1])


def getHz():
    """
     查询合租数据
     :return:
     """
    sql = "SELECT title ,text  FROM houseinfo where crawDate >='2021-01-01' and (title like '%合租%' or  text like  '%合租%' ) and title  not like '%整租%'  and  text not like '%整租%'  "
    datas = dbUtils.get_all(sql)
    hzdir = "text/zz/"
    if not os.path.exists(hzdir):
        os.mkdir(hzdir)
    for i in range(2000):
        with open(hzdir + "/h" + str(i) + ".txt", "w", encoding="utf-8") as file:
            file.write(datas[i][0] + datas[i][1])


if __name__ == '__main__':
    print("导出文本到txt开始----")
    getZz()
    getHz()
    print("导出文本到txt结束----")
