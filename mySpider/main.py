# -*- coding:UTF-8 -*-
import time
import os
import datetime

count = 0
while True:
    i = datetime.datetime.now().hour
    # 7点之前，大约一小时跑一次
    if i < 7:
        time.sleep(40)
    count = count + 1
    print("craw 当前执行次数:", count)
    os.system("scrapy crawl douban")
