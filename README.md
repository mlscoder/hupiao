# hupiao
# 马拉松程序员项目演示（上海租房信息分类）
## 沪漂小窝V2.0
![image](https://user-images.githubusercontent.com/49440936/118770069-79f9c180-b8b3-11eb-921f-d315dfc5597d.png)

## 改进
1. 出租类型改动自己训练的分类器，模型准确率在98%以上
2. 新增web端的源码
3. 新增帖子预测，预测帖子是否是中介帖子

## 文件说明
- db 数据库DDL文件
- myScrapy 爬虫功能
 * classify 分类器
    * feature_spAce 特征向量
    * models 模型
    * text 原始语料库
    * text2 分组后语料库
    * baidu_stopwords.txt 停用词
 * myScrapy Scrapy核心文件
    * mysql 数据库工具包
    * rent 信息分类工具
    * spiders 豆瓣爬虫
 * utils 公共工具包
- myweb web功能
 * static 静态文件
 * emplates 模板文件
 * app.py flas框架核心文件

## 使用步骤
### Scrapy 爬虫部分
1. 首先需要自己搭建数据库（MySQL7以上），然后在数据库中运行db文件夹中的建表语句
2. （可选）修改myScrapy/myScrapy/middlewares.py中的代理ip，源文件中使用的是[阿布云](https://www.abuyun.com/ "阿布云")付费 ，如果不使用代理，则需要设置运行速度，有可能被封ip
3. 修改myScrapy/myScrapy/mysql/MySqlUtils.py 数据库配置，根据实际情况修改
4. 修改myScrapy/classify/assess.py中get_classifier()方法中的  model_dir 和   data_dir 路径，改成自己的机器目录
5. 修改myScrapy/classify/classifier.py中的predict()方法中stopWords的路径，同样改成你的机器目录
6. 启动myScrapy/myScrapy/main.py 运行Scrapy，现在爬虫开始工作

------------
### Flask web部分

5. 修改/myWeb/app.py中app.config['SQLALCHEMY_DATABASE_URI']的值，改成实际的数据库地址和用户名和密码
6. 启动app.py,Flask查询服务启动,默认访问地址是 http://127.0.0.1:5000 


## 更新日志：
* 2021/05/19 添加按照title的相似度去重，阈值在0.65,也就是说，如果待入库的帖子在同一个创建者id下近30天有发布相似度超0.65的帖子时，不进行入库，直接pasd
