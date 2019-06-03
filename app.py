from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
app = Flask(__name__)
title = '数据集市之家'
user = {'nickname': 'Miguel'}
@app.route('/')
def index():
    return render_template('index.html',
                           #title=title,
                           user=user)
# def home():
#     return '<h1>home</h1>'

@app.route('/signin',methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
        <p><input name="username"></p>
        <p><input name="password" type="password"></p>
        <p><button type="submit">Sign In </button></p>
        </form>
        '''
@app.route('/signin',methods=['POST'])
def signin():
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return '<h3>Hello ,admin!</h3>'
    return '<h3>Bad username or password</h3>'
@app.route('/redir')
def redir():
    return redirect('https://www.baidu.com')
# @app.route('/')
# def hello_world():
#     return 'Hello World!'


if __name__ == '__main__':
    app.run()
    app.run(debug=True, host='192.168.2.69')
