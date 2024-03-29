import json
from datetime import datetime
import scrapy

from config import username, page_num
from myScrapy.items import MyscrapyItem


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['mlscoder.cn']
    page = 1
    start_urls = [f"https://hpapi.mlscoder.cn/data?username={username}&page=1"]

    def parse(self, response):
        try:
            page = response.meta['page']
        except:
            page = 1
        page = page + 1
        # 解析当前这次请求的结果
        json_object = json.loads(response.text)
        if json_object['code'] == '200':
            data = json_object['data']
            for i in data:
                item = MyscrapyItem()
                item['creator'] = i['creator']
                item['title'] = i['title']
                item['createDate'] = i['createDate']
                item['text'] = i['text']
                item['crawDate'] = datetime.now()
                item['url'] = i['url']
                yield item
        if page < page_num:
            new_url = f"https://hpapi.mlscoder.cn/data?username={username}&page={page}"
            # 回调方法，进行下一次读取
            print(new_url)
            yield scrapy.Request(url=new_url, callback=self.parse, meta={'page': page})
