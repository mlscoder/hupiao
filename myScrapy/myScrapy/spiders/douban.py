import scrapy
import json
import re
from datetime import datetime
import scrapy
from bs4 import BeautifulSoup
from myScrapy.items import MyscrapyItem
from myScrapy.mysql.MySqlUtils import MySqlUtil
from myScrapy.spiders import startUrls

city = 'sh'
dbUtil = MySqlUtil()


class DoubanSpider(scrapy.Spider):
    name = 'douban_' + city
    allowed_domains = ['douban.com']
    start_urls = startUrls.start_urls

    def parse(self, response):
        for link in getLinks(response):
            yield scrapy.Request(url=link, dont_filter=True, callback=detail, cb_kwargs={'city': city})


def getLinks(response):
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a', href=re.compile(r"^https://www.douban.com/group/topic/\d{6,11}/$"))
    linkList = []
    queryHave = "select count(*) from house_info where url=(%s) "
    for link in links:
        houses = dbUtil.get_one(queryHave, link['href'])
        if houses[0] == 0:
            linkList.append(link['href'])
    return linkList


def detail(response, city):
    """
     爬取详细内容
    :param response:
    :param city:
    :return:
    """
    soup = BeautifulSoup(response.text, 'html.parser')
    result = soup.find('script', {'type': 'application/ld+json'})

    images = soup.find_all('img', src=re.compile(r"/view/group_topic/l/public.*"))
    image_urls = []
    for image in images:
        image_url = image['src']
        image_urls.append(image_url)
    # 创建一个爬虫数据对象
    item = MyscrapyItem()
    if result is not None:
        # json 字符串转成json对象
        script = json.loads(result.string, strict=False)
        content = soup.find('a', href=re.compile("^https://www.douban.com/people/"))
        # 排序求租的帖子
        if exclude(script["name"]):
            item['creator'] = str(content['href'])[30:-1]
            item['title'] = script["name"]
            item['createDate'] = script["dateCreated"]
            item['text'] = script["text"]
            item['crawDate'] = datetime.now()
            item['url'] = script["url"]
            item['image_urls'] = image_urls
            item['city'] = city
            yield item


def exclude(text):
    """
    去除求租的帖子
    :param text:
    :return:
    """
    qiuzu_word = r'求租|找室友|求.{0,5}租'
    if re.search(qiuzu_word, text) is None:
        return True
    else:
        return False
