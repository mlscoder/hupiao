# -- coding: utf-8 --
import pandas as pda
import pymysql
import matplotlib
import matplotlib.pyplot as plt

# 设置matplotlib正常显示中文和负号
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

conn = pymysql.connect(host='101.37.124.133', user='root', passwd='Adong@123.', db='douban',
                       port=3306, charset='utf8mb4')

sql = '''
  select  station ,count(*) as num  from rent_info_temp  where station is not null  and identity =0  GROUP BY station ORDER BY num desc '''

data = pda.read_sql(sql, con=conn)
x = []
for i in data.iloc[0:10]['station']:
    x.append(i)
y = []
for i in data.iloc[0:10]['num']:
    y.append(i)
plt.figure()
plt.bar(x, y, width=0.2)
# 因为地铁站名太长，为了美观，将x轴显示旋转，
plt.xticks(rotation=270)
for a, b in zip(x, y):
    plt.text(a, b + 0.1, '%.0f' % b, ha='center', va='bottom', fontsize=10)
plt.ylabel("次数")
plt.xlabel("地铁站点")
plt.title("地铁站点出现数量分布图")
plt.show()
