from flask import Flask
from flask import Flask
import config

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)
Base = declarative_base()


class shouye(db.Model):
    __tablename__ = 'table_shouye'
    xiaobiaoti = db.Column(db.String(50))
    neirong = db.Column(db.String(1000))
    xh = db.Column(db.DECIMAL(2, 0), primary_key=True)

res =shouye.query.filter(shouye.xiaobiaoti=="数据挖掘方法").first()
print(res.neirong)
#db.create_all()

@app.route('/')
def index():
    #新增
    # blog = Blog(title="first blog",content="this is my first blog")
    # db.session.add(blog)
    # db.session.commit()

    #查询
    #res =Blog.query.filter(Blog.title=="first blog")[0]

    res =shouye.query.filter(shouye.xiaobiaoti=="数据挖掘方法").first()
    print(res.neirong)
     #修改
    # blog_edit = Blog.query.filter(Blog.title=="first blog").first()
    # blog_edit.title = "new first blog"
    # db.session.commit()
    # #删除
    # blog_delete  = Blog.query.filter(Blog.title=="first blog").first()
    # db.session.delete(blog_delete)
    # db.session.commit()
    return 'index'+res.neirong


if __name__ == '__main__':
    app.run(debug=True)