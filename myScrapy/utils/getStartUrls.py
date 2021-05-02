# -- coding: utf-8 --
# -- coding: utf-8 --
import re
import requests
from bs4 import BeautifulSoup

url = "https://www.douban.com/group/search?cat=1019&q=上海租房"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
}
response = requests.get(url, headers=headers)
# 使用BeautifulSoup对象解析html
soup = BeautifulSoup(response.text, 'html.parser')
# 查找全部href符合正则的a标签
links = soup.findAll('a', href=re.compile('^https://www.douban.com/group/.{,10}/$'))
# 创建一个set存放url，方便去重
linkUrls = set()
for link in links:
    linkUrls.add(link['href'])
print(list(linkUrls))