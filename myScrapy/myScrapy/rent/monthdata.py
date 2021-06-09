import matplotlib  # 设置matplotlib正常显示中文和负号

matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

import pandas as pda
import pymysql
import matplotlib.pyplot as plt

conn = pymysql.connect(host='101.37.124.133', user='root', passwd='Adong@123.', db='douban',
                       port=3306, charset='utf8mb4')


# 发帖次数的人数
def main():
    sql = '''
     select m.num,count(m.num) as count  from (
     select creator, count(*) as num  from house_info_temp GROUP BY creator order by num desc ) m GROUP BY m.num ORDER BY m.num desc 
    '''
    data = pda.read_sql(sql, con=conn)
    print(data)
    print(data.describe())


# 价格分布图
def priceimage():
    sql = '''
     select elt(INTERVAL(price, 0, 1000, 2000, 3000, 4000, 5000), '1/less1000', '2/1000to2000', '3/2000to3000', '4/3000to4000',  '5/4000to5000','6/moore5000') as price_level,count(id) as num 
      from monthinfo where price is not null   GROUP BY price_level ORDER BY price_level  
          '''

    data = pda.read_sql(sql, con=conn)
    x = []
    for i in data.iloc[1:6]['price_level']:
        x.append(i[2:])
    y = []
    for i in data.iloc[1:6]['num']:
        y.append(i)

    plt.figure()

    plt.bar(x, y, width=0.2, color=['g'])
    plt.xticks(x, x)
    for a, b in zip(x, y):
        plt.text(a, b + 0.1, '%.0f' % b, ha='center', va='bottom', fontsize=10)
    plt.ylabel("次数")
    plt.xlabel("价格区间")
    plt.title("价格分布图")
    plt.savefig("data/price1.png")
    plt.show()


# TOP 20 地铁站点出现数量分布图
def stationimage():
    sql = '''
     select  station ,count(*) as num  from monthinfo  where station is not null   GROUP BY station ORDER BY num desc '''

    data = pda.read_sql(sql, con=conn)
    x = []
    for i in data.iloc[0:20]['station']:
        x.append(i)
    y = []
    for i in data.iloc[0:20]['num']:
        y.append(i)
    # 生成画布
    plt.figure()

    plt.bar(x, y, width=0.2, color=['r'])
    # plt.xticks(x, x)
    plt.xticks(rotation=270)
    for a, b in zip(x, y):
        plt.text(a, b + 0.1, '%.0f' % b, ha='center', va='bottom', fontsize=10)
    plt.ylabel("次数")
    plt.xlabel("地铁站点")
    plt.title("地铁站点出现数量分布图")
    plt.savefig("data/station.png")
    plt.show()


# 地铁线路出现数量分布图
def line():
    sql = '''
    select  line ,count(*) as num  from monthinfo  where line is not null  GROUP BY line ORDER BY num desc 
    '''
    data = pda.read_sql(sql, con=conn)
    x = []
    for i in data.iloc[0:10]['line']:
        x.append(i)
    y = []
    for i in data.iloc[0:10]['num']:
        y.append(i)
    # 生成画布
    plt.figure()

    plt.bar(x, y, width=0.2, color=['black'])
    # plt.xticks(x, x)
    plt.xticks(x, x)
    for a, b in zip(x, y):
        plt.text(a, b + 0.1, '%.0f' % b, ha='center', va='bottom', fontsize=10)
    plt.ylabel("次数")
    plt.xlabel("地铁线路")
    plt.title("地铁线路出现数量分布图")
    plt.savefig("data/line.png")


# top 10小区
def address():
    sql = '''
    select  address ,count(*) as num  from monthinfo  where address is not null   GROUP BY address ORDER BY num desc 
    '''
    data = pda.read_sql(sql, con=conn)
    x = []
    for i in data.iloc[0:10]['address']:
        x.append(i)
    y = []
    for i in data.iloc[0:10]['num']:
        y.append(i)
    # 生成画布
    plt.figure()

    plt.bar(x, y, width=0.2, color=['b'])
    # plt.xticks(x, x)
    plt.xticks(rotation=270)
    for a, b in zip(x, y):
        plt.text(a, b + 0.1, '%.0f' % b, ha='center', va='bottom', fontsize=10)
    plt.ylabel("次数")
    plt.xlabel("小区名称")
    plt.title("TOP10小区出现数量分布图")
    plt.savefig("data/address.png")
    plt.show()


# 合整租分布
def renttype():
    sql = '''
    select  renttype ,count(*) as num  from monthinfo GROUP BY renttype order by renttype
    '''
    data = pda.read_sql(sql, con=conn)
    num = []
    for i in data.iloc[0:2]['num']:
        num.append(i)
    all = num[0] + num[1]

    label_list = ['合租', '整租']  # 各部分标签
    size = [num[0] / all, num[1] / all]  # 各部分大小
    color = ["r", "g"]  # 各部分颜色
    explode = [0.1, 0]  # 各部分突出值
    patches, l_text, p_text = plt.pie(size, explode=explode, colors=color, labels=label_list, labeldistance=1.1,
                                      autopct="%1.1f%%", shadow=True, startangle=90, pctdistance=0.6)
    plt.axis("equal")  # 设置横轴和纵轴大小相等，这样饼才是圆的
    plt.title("合整租分布占比")
    plt.legend()
    plt.savefig("data/renttype.png")
    plt.show()


# 仅限女生
def onlygirl():
    sql = '''
     select  onlygril ,count(*) as num  from monthinfo   GROUP BY onlygril ORDER BY onlygril desc
    '''
    data = pda.read_sql(sql, con=conn)
    num = []
    for i in data.iloc[0:2]['num']:
        num.append(i)
    all = num[0] + num[1]

    label_list = ['仅限女生', '未说明']  # 各部分标签
    size = [num[0] / all, num[1] / all]  # 各部分大小
    color = ["r", "g"]  # 各部分颜色
    explode = [0.1, 0]  # 各部分突出值
    patches, l_text, p_text = plt.pie(size, explode=explode, colors=color, labels=label_list, labeldistance=1.1,
                                      autopct="%1.1f%%", shadow=True, startangle=90, pctdistance=0.6)
    plt.axis("equal")  # 设置横轴和纵轴大小相等，这样饼才是圆的
    plt.title("仅限女生分布占比")
    plt.legend()
    plt.savefig("data/onlygirl.png")
    plt.show()


# 次数分布 柱状图
def count1():
    sql = '''
        select elt(INTERVAL(t.num, 1, 2, 3, 4, 5, 6,7), '1', '2', '3', '4',  '5','6','6+') as num_level,sum(t.count) as sum 
      from 
    (select m.num,count(m.num) as count  from (
    select creator, count(*) as num  from monthinfo GROUP BY creator order by num desc ) m GROUP BY m.num ORDER BY m.num desc ) t

     GROUP BY num_level  order by num_level 

        '''
    data = pda.read_sql(sql, con=conn)

    x = []
    for i in data.iloc[0:7]['num_level']:
        x.append(i)
    y = []
    for i in data.iloc[0:7]['sum']:
        y.append(i)
    # 生成画布
    plt.figure()

    plt.bar(x, y, width=0.2, color=['b'])
    # plt.xticks(x, x)
    plt.xticks(x, x)
    for a, b in zip(x, y):
        plt.text(a, b + 0.1, '%.0f' % b, ha='center', va='bottom', fontsize=10)
    plt.ylabel("发布人数")
    plt.xlabel("发布次数")
    plt.title("分布次数与人数")
    plt.savefig("data/count1.png")
    plt.show()


# 次数分布饼图
def count2():
    sql = '''
    select elt(INTERVAL(t.num, 1, 2, 3, 4, 5, 6,7), '1', '2', '3', '4',  '5','6','6+') as num_level,sum(t.count) as sum 
  from 
(select m.num,count(m.num) as count  from (
select creator, count(*) as num  from monthinfo GROUP BY creator order by num desc ) m GROUP BY m.num ORDER BY m.num desc ) t

 GROUP BY num_level  order by num_level 
    
    '''
    data = pda.read_sql(sql, con=conn)
    label_list = []
    for i in data.iloc[0:7]['num_level']:
        label_list.append(i)
    num = []
    for i in data.iloc[0:7]['sum']:
        num.append(i)

    all = num[0] + num[1] + num[2] + num[3] + num[4] + num[5] + num[6]

    # label_list = ['仅限女生', '未说明']  # 各部分标签
    size = [num[0] / all, num[1] / all, num[2] / all, num[3] / all, num[4] / all, num[5] / all, num[6] / all]  # 各部分大小
    color = ["r", "g", "b", "y", "orange", "fuchsia", "pink"]  # 各部分颜色
    explode = [0.1, 0, 0, 0, 0, 0, 0]  # 各部分突出值
    patches, l_text, p_text = plt.pie(size, explode=explode, colors=color, labels=label_list, labeldistance=1.1,
                                      autopct="%1.1f%%", shadow=True, startangle=90, pctdistance=0.6)
    plt.axis("equal")  # 设置横轴和纵轴大小相等，这样饼才是圆的
    plt.title("分布次数人数占比")
    plt.legend()
    plt.savefig("data/count2.png")
    plt.show()


# 支付类型分布
def pay():
    sql = '''
    select  pay ,count(*) as num  from monthinfo GROUP BY pay order by pay 
    '''
    data = pda.read_sql(sql, con=conn)
    num = []
    for i in data.iloc[0:3]['num']:
        num.append(i)
    all = num[0] + num[1] + num[2]

    label_list = ['未说明或其他', '押一付一', '押一付三']  # 各部分标签
    size = [num[0] / all, num[1] / all, num[2] / all]  # 各部分大小
    color = ["r", "g", "b"]  # 各部分颜色
    explode = [0.1, 0, 0]  # 各部分突出值
    patches, l_text, p_text = plt.pie(size, explode=explode, colors=color, labels=label_list, labeldistance=1.1,
                                      autopct="%1.1f%%", shadow=True, startangle=90, pctdistance=0.6)
    plt.axis("equal")  # 设置横轴和纵轴大小相等，这样饼才是圆的
    plt.title("支付类型分布占比")
    plt.legend()
    plt.savefig("data/pay.png")
    plt.show()


# 价格分布图
def price():
    sql = '''
     select elt(INTERVAL(price, 0, 1000, 2000, 3000, 4000, 5000), '1/less1000', '2/1000to2000', '3/2000to3000', '4/3000to4000',  '5/4000to5000','6/moore5000') as price_level,count(id) as num 
      from monthinfo where price is not null   GROUP BY price_level ORDER BY price_level  
'''

    data = pda.read_sql(sql, con=conn)
    x = []
    for i in data.iloc[1:6]['price_level']:
        x.append(i[2:])
    num = []
    for i in data.iloc[1:6]['num']:
        num.append(i)
    all = num[0] + num[1] + num[2] + num[3] + num[4]
    label_list = ['1-2k', '2-3k', '3-4k', '4-5k', '5k+', ]  # 各部分标签
    size = [num[0] / all, num[1] / all, num[2] / all, num[3] / all, num[4] / all]  # 各部分大小
    color = ["r", "g", "b", "y", "orange"]  # 各部分颜色
    explode = [0.1, 0.1, 0, 0, 0]  # 各部分突出值
    patches, l_text, p_text = plt.pie(size, explode=explode, colors=color, labels=label_list, labeldistance=1.1,
                                      autopct="%1.1f%%", shadow=True, startangle=90, pctdistance=0.6)
    plt.axis("equal")  # 设置横轴和纵轴大小相等，这样饼才是圆的
    plt.title("价格分布占比")
    plt.legend()
    plt.savefig("data/price2.png")
    plt.show()


def bingtu():
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']
    matplotlib.rcParams['axes.unicode_minus'] = False

    label_list = ['1次', '2次', '3次', '4次', '5次', '6次', '7次', '大于7次']  # 各部分标签
    size = [4293 / 11025, 1937 / 11025, 1129 / 11025, 812 / 11025, 520 / 11025, 380 / 11025, 306 / 11025,
            1648 / 11025]  # 各部分大小
    color = ["r", "g", "b", "y", "black", "orange", "fuchsia", "pink"]  # 各部分颜色
    explode = [0, 0, 0, 0, 0, 0, 0, 0]  # 各部分突出值
    patches, l_text, p_text = plt.pie(size, explode=explode, colors=color, labels=label_list, labeldistance=1.1,
                                      autopct="%1.1f%%", shadow=True, startangle=90, pctdistance=0.6)
    plt.axis("equal")  # 设置横轴和纵轴大小相等，这样饼才是圆的
    plt.title("发布次数占比")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
    # count1()
    # count2()
    # renttype()
    # pay()
    # onlygirl()
    # priceimage()
    # price()
    # stationimage()
# line()
# address()
