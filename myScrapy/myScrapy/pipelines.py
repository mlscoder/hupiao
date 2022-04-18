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
        print(result)
        haveOne = [item["creator"]]

        # 查询同一个创建者最近一个月发布的帖子
        querySql = "select title from house_info where creator=(%s)  and crawDate >= DATE_SUB(NOW(),INTERVAL 30 day)"
        houses = dbUtil.get_all(querySql, haveOne)
        # 如果存在相同的帖子则不保存
        print("------------------")
        print(houses, item["title"])
        print(rentClassify.check(houses, item["title"]))
        if rentClassify.check(houses, item["title"]):
            saveSql = "insert into house_info (title, createDate, text,crawDate,url,creator) values (%s,%s,%s,%s,%s,%s)"
            h_id = dbUtil.save(saveSql, result)
            # 分析租房信息的分类
            info = rentClassify.analysis(item["url"], item["creator"], item["title"] + item["text"])
            # 添加租房信息的id
            info.append(h_id)
            infoSaveSql = "insert into rent_info (url, station, `identity`,price,pay,only_girl,rent_type,`count`,create_date,h_id) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

            # 保存信息分类
            print(info)
            # 这里是入库，我没有写了，因为我的数据库里有了这些。
            #  r_id = dbUtil.save(infoSaveSql, info)
        return item
