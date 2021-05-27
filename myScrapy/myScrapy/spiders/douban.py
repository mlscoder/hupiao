import scrapy
import json
import re
from datetime import datetime
import scrapy
from bs4 import BeautifulSoup
from myScrapy.items import MyscrapyItem
from myScrapy.spiders import startUrls

city = 'sh'
class DoubanSpider(scrapy.Spider):
    name = 'douban_' + city
    allowed_domains = ['douban.com']
    start_urls = startUrls.start_urls

    def parse(self, response):
        for link in getLinks(response):
            yield scrapy.Request(url=link['href'], dont_filter=True, callback=detail, cb_kwargs={'city': city})


def getLinks(response):
    soup = BeautifulSoup(response.text, 'html.parser')
    # 选取所有标签tr 且class属性等于even或odd的元素
    links = soup.find_all('a', href=re.compile(r"^https://www.douban.com/group/topic/\d{6,11}/$"))
    return links


def parse(response):
    soup = BeautifulSoup(response.text, 'html.parser')
    # 选取所有标签tr 且class属性等于even或odd的元素
    links = soup.find_all('a', href=re.compile(r"^https://www.douban.com/group/topic/\d{6,11}/$"))
    for link in links:
        new_url = link['href']
        # 请求详细页,请求完成后调用回调函数--detail
        yield scrapy.Request(url=new_url, dont_filter=True, callback=detail, cb_kwargs={'city': 'sh'})


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
        # 截取出信息创建者的豆瓣id
        item['creator'] = str(content['href'])[30:-1]
        item['title'] = script["name"]
        item['createDate'] = script["dateCreated"]
        item['text'] = script["text"]
        item['crawDate'] = datetime.now()
        item['url'] = script["url"]
        item['image_urls'] = image_urls
        item['city'] = city
        yield item
