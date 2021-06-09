# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from myScrapy.mysql.MySqlUtils import MySqlUtil
from myScrapy.rent import rentClassify

dbUtil = MySqlUtil()


class MyscrapyPipeline:
    def process_item(self, item, spider):
        result = [item["title"], item["createDate"], item["text"], item["crawDate"], item["url"], item["creator"]]
        haveOne = [item["creator"]]
        city = item["city"]
        image_urls = item["image_urls"]

        querySql = "select title from house_info where creator=(%s)  and crawDate >= DATE_SUB(NOW(),INTERVAL 30 day)"
        houses = dbUtil.get_all(querySql, haveOne)
        # 储存原始信息
        saveSql = "insert into house_info (title, createDate, text,crawDate,url,creator) values (%s,%s,%s,%s,%s,%s)"

        h_id = dbUtil.save(saveSql, result)
        # 如果存在相似度很高的帖子，则不进行分析
        if rentClassify.check(houses, item["title"]):
            # 分析租房信息的分类
            info = rentClassify.analysis(item["url"], item["creator"], city, item["title"] + item["text"])
            # 添加租房信息的id
            info.append(h_id)
            info.append(city)
            infoSaveSql = "insert into rent_info (url, station, `identity`,price,pay,only_girl,rent_type,`count`,create_date,h_id,city) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            # 保存信息分类
            r_id = dbUtil.save(infoSaveSql, info)
            # 图片链接保存
            if len(image_urls) > 0:
                imageSql = "INSERT INTO image(r_id,url) VALUES (%s,%s)"
                for image_url in image_urls:
                    i = [r_id, image_url]
                    dbUtil.save(imageSql, i)
        return item
