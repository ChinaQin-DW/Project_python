# -- coding:utf-8 --
from flask import Flask,render_template,request,redirect,url_for,session
import config
from models import table_shouye
from exts import db
app=Flask(__name__)
app.config.from_object(config)
db.init_app(app)
# 初始化db,并创建models中定义的表格
with app.app_context():  # 添加这一句，否则会报数据库找不到application和context错误
    db.init_app(app)  # 初始化db
    db.create_all()  # 创建所有未创建的table
#print(table_shouye.query.all())

# 首页函数
@app.route('/')
def index():
    context = table_shouye.query.all()
    return 'hello'+str(context[0])

if __name__=='__main__':
    app.run()


