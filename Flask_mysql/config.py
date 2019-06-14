# -- coding:utf-8 --
import os

DEBUG=True

SECRET_KEY=os.urandom(24)

# 数据库配置
HOSTNAME='119.27.184.139'
PORT='3306'
DATABASE='china'
USERNAME='china'
PASSWORD='chinaqin123'
DB_URI='mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI=DB_URI

SQLALCHEMY_TRACK_MODIFICATIONS=False
