# -*- coding:utf-8 -*-
from flask import Flask
from werkzeug.routing import BaseConverter

class Regex_url(BaseConverter):
    def __init__(self,url_map,*args):
        super(Regex_url,self).__init__(url_map)
        self.regex = args[0]

app = Flask(__name__)
app.url_map.converters['re'] = Regex_url


@app.route('/user/<re("[a-z]{3}"):id>')
def hello_itcast1(id):
    return 'hello %s' %id


#设置cookie：
from flask import make_response
@app.route('/cookie')
def set_cookie():
    resp = make_response('this is to set cookie')
    resp.set_cookie('username', 'itcast')
    return resp


#获取cookie
from flask import request
@app.route('/request')
def resp_cookie():
    resp = request.cookies.get('username')
    return resp

#获取当前的appname
# from flask import current_app
# @app.route('/')
# def text():
#     return current_app.name
from flask import render_template
@app.route('/')
def hello_itcast():
    return render_template('text.html')

@app.route('/user/<name>')
def hello_user(name):
    return render_template('text.html', name=name)


@app.route('/index')
def index():
    mydict = {'key':'silence is gold'}
    mylist = ['Speech', 'is','silver']
    myintvar = 0

    return render_template('vars.html',
                           mydict=mydict,
                           mylist=mylist,
                           myintvar=myintvar
                           )


#命令行启动，并固定IP访问
from flask_script import Manager
# manager = Manager(app)
# manager.run()

if __name__ == '__main__':
    app.run()

