# -- coding: utf-8 --
import time
import os
import datetime

while True:
    i = datetime.datetime.now().hour
    # 7点之前，大约40跑一次

    # if i < 7:
    #   time.sleep(60)
    os.system("scrapy crawl douban")
