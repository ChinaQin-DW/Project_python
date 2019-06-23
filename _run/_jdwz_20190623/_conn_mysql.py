# -- coding:utf-8 --
import pymysql
def select_mysql():
    # 打开数据库连接
    db = pymysql.connect("119.27.184.139", "china", "chinaqin123", "china")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql = "select wzip from ip_jc;"
    # 执行SQL语句
    cursor.execute(sql)
    results = cursor.fetchall()
    db.close()
    return results
