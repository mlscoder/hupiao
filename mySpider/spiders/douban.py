# -*- coding: utf-8 -*-
import json
import re
from datetime import datetime
import scrapy
from bs4 import BeautifulSoup
from lxml import etree

from mySpider.items import MyspiderItem
from mySpider.mysql.mysql_DBUtils import MyPymysqlPool
from mySpider.spiders import groupurls


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['www.douban.com']

    # 测试url start_urlsteststart_urls
    start_urls = groupurls.start_urls

    def parse(self, response):
        # new_urls = self.parser.parseUrl(response.request.url, response.text,r"/group/topic/.")
        # self.topicurls.add_new_urls(new_urls)
        # print("总计urls" + str(self.topicurls.url_count()))

        soup = BeautifulSoup(response.text, 'html.parser')
        # 选取所有标签tr 且class属性等于even或odd的元素
        links = soup.find_all('a', href=re.compile(r"/group/topic/.*"))
        for link in links:

            new_url = link['href']
            # yield item  注释yield item ，因为detail方法中yield item会覆盖这个
            # 请求详细页,请求完成后调用回调函数--detail

            if self.isexist(new_url):
                yield scrapy.Request(url=new_url, callback=self.detail)
            '''
            实例化对象要放在循环里面，否则会造成item被多次赋值，
            因为每次循环完毕后，请求只给了调度器，入队，并没有去执行请求，
            循环完毕后，下载器会异步执行队列中的请求,此时item已经为最后一条记录，
            而详细内容根据url不同去请求的，所以每条详细页是完整的，
            最终结果是数据内容为每页最后一条，详细内容与数据内容不一致，
            在yield item后，会把内容写到pipeline中
            '''

    def detail(self, response):
        """
        爬取详细内容
        :param response:
        :return:
        """

        soup = BeautifulSoup(response.text, 'html.parser')
        item = MyspiderItem()
        selector = etree.HTML(response.text)
        result = soup.find('script', {'type': 'application/ld+json'})
        if result != None:
            script = json.loads(result.get_text(), strict=False)
            content = selector.xpath('//*[@id="content"]/div/div[1]/div[1]/div[2]/h3/span[1]/a/@href')  #
            d1 = datetime.now()
            d2 = datetime.fromisoformat((script["dateCreated"]))
            item['creator'] = str(content[0])[30:-1]  # 截取出信息创建者的豆瓣id
            item['title'] = script["name"]
            item['createDate'] = script["dateCreated"]
            item['text'] = script["text"]
            item['crawDate'] = datetime.now()
            item['url'] = script["url"]
            # 只获取最近30天发布的帖子
            if ((d1 - d2).days < 30):
                yield item

    @staticmethod
    def isexist(url):
        sql = "select count(*) from houseinfo where url=(%s)"
        mysql = MyPymysqlPool("dbMysql")
        count = mysql.getAll(sql, url)
        if count[0]['count(*)'] == 0:
            return True
        return False
