# -- coding:utf-8 --
DEBUG = True
#dialect+driver://root:1q2w3e4r5t@127.0.0.1:3306/
DIALECT = 'mysql'
DRIVER='pymysql'
USERNAME = 'china'
PASSWORD = 'chinaqin123'
HOST = '119.27.184.139'
PORT = 3306
DATABASE = 'china'

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = False
print(SQLALCHEMY_DATABASE_URI)