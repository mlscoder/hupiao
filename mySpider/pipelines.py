# -*- coding: utf-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import re

from mySpider.mysql.mysql_DBUtils import MyPymysqlPool

import mySpider.rent as rent


class MyspiderPipeline(object):

    def open_spider(self, spider):
        self.mysql = MyPymysqlPool("dbMysql")
        pass

    def process_item(self, item, spider):
        result = (item["title"], item["createDate"], item["text"], item["crawDate"], item["url"], item["creator"])
        title = item["title"]
        text = item["text"]
        creator = item["creator"]
        url = item["url"]
        isone = [title, creator]
        # 查询sql
        sql1 = "select count(*) from houseinfo  where title =(%s) and  creator=(%s)"

        # 新增sql
        sql = "INSERT INTO houseinfo(title, createDate, text,crawDate,url,creator) VALUES (%s,%s,%s,%s,%s,%s)"
        # 租房信息处理后的插入到数据库中的操作。
        rentsql = "INSERT INTO rentinfo(hid, price, address,line,station,renttype,landlord,pay,count,createDate,onlygril,title,url) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

        id = None
        try:
            # 查询同一个人是否写过同一个标题的帖子，排除发在多个小组的情况
            queryresult = self.mysql.getOne(sql1, isone)
            if queryresult["count(*)"] == 0:
                id = self.mysql.insert(sql, result)
        except Exception as e:
            print("MyspiderPipeline出错---")
        if id != None:
            rq = rent.anay(id, title, creator, text)
            if rq != None:
                t = [rq.hid, rq.price, rq.address, rq.line, rq.station, rq.renttype, rq.landlord, rq.pay, rq.count,
                     rq.createDate, rq.onlygril, title, url]

                self.mysql.insert(rentsql, t)
        self.mysql.end()
        return item

    def close_spider(self, spider):
        self.mysql.dispose()
