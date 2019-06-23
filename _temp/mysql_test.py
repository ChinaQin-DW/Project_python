# -- coding:utf-8 --
import pymysql

fx='总成绩20'
xh=1
wzkh='1111'
# 打开数据库连接
db = pymysql.connect("119.27.184.139", "china", "chinaqin123", "china")
# 使用cursor()方法获取操作游标
cursor = db.cursor()
# SQL 更新语句
sql = "UPDATE jdwz_2 SET fx = '%s',wzkh='%s' WHERE xh = '%d';" % (fx,wzkh,xh)
cursor.execute(sql)
db.commit()
db.close()
