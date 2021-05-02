# hupiao
# 马拉松程序员项目演示（上海租房信息分类）
## 沪漂小窝V2.0

## 改进
1. 出租类型改动自己训练的分类器，模型准确率在98%以上
2. 新增web端的源码
3. 新增帖子预测，预测帖子是否是中介帖子

## 文件说明
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
