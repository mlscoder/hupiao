import datetime
import json

from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:mlscoder.@101.37.124.133:3306/douban?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
# 关联app
db = SQLAlchemy(app)


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

    # 这个关系允许在score表中使用studnet 来显示 表studnet中所有内容
    # 在表student中使用my_score来显示 score表中所有内容
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


# 查询页面
@app.route('/', methods=['GET', 'POST'])
def query_page():
    # 从表单接收参数，get与<input>的name属性值相同
    pageSize = 10;  # 设置每页条数
    currentPage = request.form.get('currentPage')
    price = request.form.get('price')
    station = request.form.get('station')
    only_girl = request.form.get('only_girl')
    pay = request.form.get('pay')
    rent_type = request.form.get('rent_type')
    count = request.form.get('count')
    search = []
    # 如果条件不为空，添加到search列表中
    if currentPage is None or currentPage == "NaN":
        currentPage = 1

    if price is not None and price != '':
        search.append(RentInfo.price <= price.strip())
    if station is not None and station != '':
        search.append(RentInfo.station == station.strip())
    if only_girl is not None and only_girl != '不限':
        search.append(RentInfo.only_girl == only_girl)
    if pay is not None and pay != '不限':
        search.append(RentInfo.pay == pay)
    if rent_type is not None and rent_type != '不限':
        search.append(RentInfo.rent_type == rent_type)
    if count is not None and count != "" and int(count) > 0:
        search.append(RentInfo.count <= int(count) - 1)
    # 查询中添加上分页
    rents = RentInfo.query.filter(*search).order_by(RentInfo.id.desc()).limit(pageSize).offset(
        (int(currentPage) - 1) * pageSize)
    # 计算总条数
    pageCount = RentInfo.query.filter(*search).count()
    return render_template('index.html', rents=rents, price=price,
                           station=station,
                           only_girl=only_girl, pay=pay,
                           rent_type=rent_type, count=count,
                           pageSize=pageSize, currentPage=currentPage, pageCount=pageCount)


if __name__ == "__main__":
    # 将host设置为0.0.0.0，则外网用户也可以访问到这个服务
    app.run(debug=True)
