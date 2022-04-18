# DB配置 当前仅支持【mysql】
host = "127.0.0.1"
port = 3306
name = "root"
password = "root"
# 数据库名字，使用utf8mb4，也可以自定义
dbname = "douban"

# 此文件的目录。本地下载后需要更改一下，在引用分类模型的时候使用
project_path = "E:\\share\\hupiao"

# [下面两个参数用在douban.py文件中]
# 这是数据接口的api授权用户名。联系mlscoder获取
username = "mlscoder"
# 数据api接口提供16w的数据，每页100条数据
# 设置爬取的页数，全量是1641页，测试的时候可以设置3，可以快速看结果。
page_num = 3
