import scrapy
from myScrapy.spiders import startUrls, douban

city = 'bj'


class DoubanSpider(scrapy.Spider):
    name = 'douban_' + city
    allowed_domains = ['douban.com']
    start_urls = startUrls.cityUrlsDict.get(city)

    def parse(self, response):
        for link in douban.getLinks(response):
            yield scrapy.Request(url=link, dont_filter=True, callback=douban.detail, cb_kwargs={'city': city})
