# 沪漂小窝租房信息分类系统（学习项目）

## 演示PC端：https://hupiao.mlscoder.cn/

## 演示移动端：小程序【租房搜索助手】

#### 由于豆瓣的原因，关闭了租房类小组，所以爬虫已经失效，本项目改成学习项目，详情看learn分支

### learn分支：项目学习分支，请使用此分支，提供数据Api接口

### master分支是沪漂小窝v3.0,单城市（仅上海）版本

### manycities分支是沪漂小窝v4.0,多城市版本。

    目前支持的城市：上海、北京、广州、深圳、杭州、南京、武汉、重庆、成都。

#### v3页面

![image](https://user-images.githubusercontent.com/49440936/118770069-79f9c180-b8b3-11eb-921f-d315dfc5597d.png)

#### v4页面

![image](https://user-images.githubusercontent.com/49440936/119754742-74176800-bed3-11eb-9d25-5bbb99a77c12.png)

## 使用步骤 

### 环境配置部分

0. 先安装环境，相关包参考requirements.txt,文件中可能不是最新版本的,不确定最新版的包是否存在兼容问题
1. 首先需要自己搭建数据库（MySQL7以上），然后在数据库中运行db文件夹中的建表语句
2. 修改config.py 数据库配置，根据实际情况修改

------------

### Scrapy 爬虫部分

3. （可选）修改myScrapy/myScrapy/middlewares.py中的代理ip，源文件中使用的是[阿布云](https://www.abuyun.com/ "阿布云")付费
   ，如果不使用代理，则需要设置运行速度，有可能被封ip
4. 启动myScrapy/myScrapy/main.py 运行Scrapy，现在爬虫开始工作

------------

### Flask web部分

5. 直接启动 python app.py,Flask查询服务启动,默认访问地址是 http://127.0.0.1:5000

## 代理选择

* 本次测试推荐使用:阿布云（1元/小时起）,长期使用推荐：蘑菇代理（80元/月起）。具体的使用配置参考代理运营商文档

## 更新日志：

* 2021/08/17 更新数据库配置文件
* 2021/08/17 更新项目依赖包文件
* 2021/06/09 修复并发下载内容重复的问题
* 2021/06/01 添加搜中介功能
* 2021/05/27 提交多版本代码,在manycities分支上，master分支需要配合案例，并没有合并
* 2021/05/25 创建新的分支-manycities,用于多城市版本的开发
* 2021/05/24 修改文件路径为相对路径，减少配置项目
* 2021/05/19 添加按照title的相似度去重，阈值在0.65,也就是说，如果待入库的帖子在同一个创建者id下近30天有发布相似度超0.65的帖子时，不进行入库，直接pasd

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
    * spiders 豆瓣爬虫 (包含9个城市的爬虫)
* utils 公共工具包

- myweb web功能

* static 静态文件
* emplates 模板文件
* app.py flas框架核心文件

## 联系作者

添加微信【mlscoder】
