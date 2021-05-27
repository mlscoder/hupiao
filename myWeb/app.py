import datetime
import json

from flask import Flask, render_template, request, jsonify, Response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

app = Flask(__name__)

app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:adong123.@172.16.32.4:3306/douban?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
# 关联app
db = SQLAlchemy(app)

# 城市映射字典表
cityName = {
    'sh': '上海',
    'bj': '北京',
    'gz': '广州',
    'sz': '深圳',
    'hz': '杭州',
    'nj': '南京',
    'wh': '武汉',
    'cd': '成都',
    'cq': '重庆'
}


class Subway(db.Model):
    """
    地铁模型类
    """
    __tablename__ = 'subways'
    id = db.Column(db.Integer, primary_key=True)
    subway_line_id = db.Column(db.String)
    subway_line_name = db.Column(db.String)
    subway_name = db.Column(db.String)
    sort_index = db.Column(db.String)
    city_code = db.Column(db.Date)
    sort_line = db.Column(db.Date)


class HouseInfo(db.Model):
    """
    房源信息模型类
    """
    __tablename__ = 'house_info'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    text = db.Column(db.String)
    url = db.Column(db.String)
    creator = db.Column(db.String)
    createDate = db.Column(db.Date)
    crawDate = db.Column(db.Date)


class RentInfo(db.Model):
    houseInfo = relationship("HouseInfo")
    """
    租房分类信息模型类
    """
    __tablename__ = 'rent_info'
    id = db.Column(db.Integer, primary_key=True)
    h_id = db.Column(db.Integer, ForeignKey('house_info.id'))
    url = db.Column(db.String)
    station = db.Column(db.String)
    identity = db.Column(db.String)
    price = db.Column(db.String)
    pay = db.Column(db.String)
    rent_type = db.Column(db.String)
    only_girl = db.Column(db.String)
    count = db.Column(db.String)
    create_date = db.Column(db.String)
    city = db.Column(db.String)

    # 这个relationship 是orm自己的东西，和mysql无关，是类之间的调用

    def __str__(self):
        return "id:{0},url:{1},地址:{2},身份预测:{3},价格:{4},支付方式:{5},出租方式:{6},仅限女生:{7},发帖次数:{8},创建时间:{9}". \
            format(self.id, self.url, self.station, self.identity,
                   self.price, self.pay, self.rent_type, self.only_girl, self.count, self.create_date)

    def object2dict(self):
        rent = {"id": self.id,
                "url": self.url,
                "station": self.station,
                "identity": self.identity,
                "price": self.price,
                "pay": self.pay,
                "rent_type": self.rent_type,
                "only_girl": self.only_girl,
                "count": self.count,
                "create_date": self.create_date}
        return rent


@app.route('/getSubwayStation', methods=['GET'])
def getSubwayStation():
    city = request.args.get("city")
    line_name = request.args.get("line")
    search = []
    search.append(Subway.city_code == city)
    search.append(Subway.subway_line_name == line_name)
    subways = Subway.query.filter(*search)
    stationList = []
    for subway in subways:
        stationList.append(subway.subway_name)
    jsonArr = json.dumps(stationList, ensure_ascii=False)
    return jsonArr


# 查询页面
@app.route('/', methods=['GET', 'POST'])
def query_page():
    city = request.args.get("city")
    if city is None:
        city = 'sh'

    # 从表单接收参数，get与<input>的name属性值相同
    pageSize = 10  # 设置每页条数
    currentPage = request.form.get('currentPage')
    price = request.form.get('price')
    station = request.form.get('station')
    only_girl = request.form.get('only_girl')
    pay = request.form.get('pay')
    rent_type = request.form.get('rent_type')
    count = request.form.get('count')
    lineName = request.form.get('line')

    search = []
    search.append(RentInfo.city == city)
    # 如果条件不为空，添加到search列表中
    if currentPage is None or currentPage == "NaN":
        currentPage = 1

    if price is not None and price != '':
        if price == '1':
            search.append(RentInfo.price <= '1500')
        if price == '2':
            search.append(RentInfo.price >= '1500')
            search.append(RentInfo.price <= '2500')
        if price == '3':
            search.append(RentInfo.price >= '2500')
            search.append(RentInfo.price <= '3500')
        if price == '4':
            search.append(RentInfo.price >= '3500')
            
    if station is not None and station != ''and station != '地铁站点':
        search.append(RentInfo.station == station.strip())
    if only_girl is not None and only_girl != '不限':
        search.append(RentInfo.only_girl == only_girl)
    if pay is not None and pay != '不限':
        search.append(RentInfo.pay == pay)
    if rent_type is not None and rent_type != '不限':
        search.append(RentInfo.rent_type == rent_type)
    search.append(RentInfo.create_date >= str(get_days_before_today(15)))

    # 查询中添加上分页
    rents = RentInfo.query.filter(*search).order_by(RentInfo.id.desc()).limit(pageSize).offset(
        (int(currentPage) - 1) * pageSize)
    rents = list(rents)
    for rent in rents:
        h_id = rent.h_id
        sql = 'select count(*) from  house_info  where   crawDate >= DATE_SUB(NOW(),INTERVAL 30 day)  and  creator =(select creator from house_info where  id= :h_id)'
        count = db.session.execute(sql, {'h_id': h_id})
        month = list(count)
        rent.monthSum = month[0][0]
    # 计算总条数
    pageCount = RentInfo.query.filter(*search).count()
    if pageCount > 400:
        pageCount = 400

    sql = 'select distinct subway_line_name from  subways  where city_code=:cityCode '
    line_names = db.session.execute(sql, {'cityCode': city})
    lines = list(line_names)
    lineList = []
    for line in lines:
        lineList.append(line[0])
    return render_template('index.html', rents=rents, price=price,
                           station=station,
                           only_girl=only_girl, pay=pay,
                           rent_type=rent_type, count=count,
                           cityName=cityName.get(city),
                           cityCode=city, lines=lineList,lineName=lineName,
                           pageSize=pageSize, currentPage=currentPage, pageCount=pageCount)


# 获取当前时间点前n天的时间
def get_days_before_today(n=0):
    '''''
    date format = "YYYY-MM-DD HH:MM:SS"
    '''
    now = datetime.datetime.now()
    if (n < 0):
        return datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
    else:
        n_days_before = now - datetime.timedelta(days=n)
    return datetime.datetime(n_days_before.year, n_days_before.month, n_days_before.day, n_days_before.hour,
                             n_days_before.minute, n_days_before.second)



if __name__ == "__main__":
    # 将host设置为0.0.0.0，则外网用户也可以访问到这个服务
    app.run(host="127.0.0.1", port=5000, debug=True)
