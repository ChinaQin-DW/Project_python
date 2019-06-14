from flask import Flask
from datetime import datetime
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
import config

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)
Base = declarative_base()

##创建model
class shouye(db.Model):
    __tablename__ = 'table_shouye'
    xiaobiaoti = db.Column(db.String(50))
    neirong = db.Column(db.String(1000))
    xh = db.Column(db.DECIMAL(2, 0), primary_key=True)
#查询
res =shouye.query.filter(shouye.xiaobiaoti=="数据挖掘方法").first()
print(res.neirong)
#修改
# shouye = shouye(title="first blog",content="this is my first blog")
# db.session.add(shouye)
# db.session.commit()
#修改
    # blog_edit = Blog.query.filter(Blog.title=="first blog").first()
    # blog_edit.title = "new first blog"
    # db.session.commit()
#删除
# blog_delete  = Blog.query.filter(Blog.title=="first blog").first()
# db.session.delete(blog_delete)
# db.session.commit()

@app.route('/')  #methods=['GET']
@app.route('/home')
def home():
    return render_template(
        'index.html',
         title= res.xiaobiaoti,##"数据之家",
         year=datetime.now().year
    )
@app.route('/contact')
def contact():
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/source')
def source():
    return render_template(
        'source.html',
        title='source',
        year=datetime.now().year,
        message='Your application description page.'
    )
if __name__ == '__main__':
    app.run(debug=True)
