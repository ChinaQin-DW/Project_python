from flask import Flask
from datetime import datetime
from flask import render_template
#from models import TableShouye
app = Flask(__name__)
#results = TableShouye.query.all()
#print(results)
@app.route('/')  #methods=['GET']
@app.route('/home')
def home():
    return render_template(
        'index.html',
         title="数据之家",
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
