# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import base64
import hashlib
import time

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
from scrapy.utils.response import response_status_message


class MyscrapySpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


import base64

# 代理服务器
proxyServer = "http://http-dyn.abuyun.com:9020"
# 代理隧道验证信息
proxyUser = "H5J492Y13VHEV62D"
proxyPass = "B8C90D2255566DFC"
proxyAuth = "Basic " + base64.urlsafe_b64encode(bytes((proxyUser + ":" + proxyPass), "ascii")).decode("utf8")


class MyscrapyDownloaderMiddleware:
    def process_request(self, request, spider):
        request.meta["proxy"] = proxyServer
        request.headers["Proxy-Authorization"] = proxyAuth

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_response(self, request, response, spider):
        if request.meta.get('dont_retry', False):
            return response
        elif response.status == 429:
            self.crawler.engine.pause()
            time.sleep(6)  # If the rate limit is renewed in a minute, put 60 seconds, and so on.
            self.crawler.engine.unpause()
            reason = response_status_message(response.status)
            return self._retry(request, reason, spider) or response
        elif response.status in self.retry_http_codes:
            reason = response_status_message(response.status)
            return self._retry(request, reason, spider) or response
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class myProxy(object):
    def __init__(self, crawler):
        super(myProxy, self).__init__()
        self.appkey = "103351821"
        self.secret = "0651241404a190e6dacc4935e4305ccc"
        self.mayi_url = 's2.proxy.mayidaili.com'
        self.mayi_port = '8123'

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def get_proxy_authorization(self):
        paramMap = {
            "app_key": self.appkey,
            # 如果你的程序在国外，请进行时区处理
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        # 排序
        keys = paramMap.keys()
        codes = "%s%s%s" % (self.secret, str().join('%s%s' %
                                                    (key, paramMap[key]) for key in keys), self.secret)
        # 计算签名
        sign = hashlib.md5(codes.encode()).hexdigest().upper()
        paramMap["sign"] = sign
        # 拼装请求头Proxy-Authorization的值
        keys = paramMap.keys()
        authHeader = "MYH-AUTH-MD5 " + \
                     str('&').join('%s=%s' % (key, paramMap[key]) for key in keys)
        return authHeader

    def get_proxy_url(self):
        return 'http://{}:{}'.format(self.mayi_url, self.mayi_port)

    def process_request(self, request, spider):
        request.meta['proxy'] = self.get_proxy_url()
        request.headers['Mayi-Authorization'] = self.get_proxy_authorization()

    def process_response(self, request, response, spider):
        if response.status != 200:
            return request
        return response
