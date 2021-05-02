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
        haveOne = [item["title"], item["creator"]]

        # 查询同一个创建者发布的同一标题的帖子，方便去重。
        querySql = "select count(*) from house_info  where title =(%s) and  creator=(%s)"
        size = dbUtil.get_one(querySql, haveOne)
        # 如果存在相同的帖子则不保存
        if size[0] == 0:
            saveSql = "insert into house_info (title, createDate, text,crawDate,url,creator) values (%s,%s,%s,%s,%s,%s)"
            h_id = dbUtil.save(saveSql, result)
            # 分析租房信息的分类
            info = rentClassify.analysis(item["url"], item["creator"], item["title"] + item["text"])
            # 添加租房信息的id
            info.append(h_id)
            infoSaveSql = "insert into rent_info (url, station, `identity`,price,pay,only_girl,rent_type,`count`,create_date,h_id) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            # 保存信息分类
            dbUtil.save(infoSaveSql, info)
        return item
