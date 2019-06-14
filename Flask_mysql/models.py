# -- coding:utf-8 --
from exts import db
# 定义用户模型
class table_shouye(db.Model):
    __tablename__ = 'table_shouye'
    xiaobiaoti = db.Column(db.String(50))
    neirong = db.Column(db.String(1000))
    xh = db.Column(db.DECIMAL(2, 0), primary_key=True)
