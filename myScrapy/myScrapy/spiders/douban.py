import scrapy
import json
import re
from datetime import datetime
import scrapy
from bs4 import BeautifulSoup
from myScrapy.items import MyscrapyItem
from myScrapy.spiders import startUrls


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = startUrls.start_urls

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        # 选取所有标签tr 且class属性等于even或odd的元素
        links = soup.find_all('a', href=re.compile(r"/group/topic/.*"))
        for link in links:
            new_url = link['href']
            # yield item  注释yield item ，因为detail方法中yield item会覆盖这个
            # 请求详细页,请求完成后调用回调函数--detail
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
        result = soup.find('script', {'type': 'application/ld+json'})
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
            yield item
