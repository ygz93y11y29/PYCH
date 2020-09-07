# -*- coding:utf-8 -*-
from flask import Flask,render_template,request,make_response
app = Flask(__name__)


###当访问URL时，会打开一个简单的表单
@app.route('/')
def index():
   return render_template('index1.html')
##表单发布到'/ setcookie' URL，相关联的视图函数设置Cookie名称userID并呈现另一个页面
@app.route('/setcookie', methods=['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['nm']

    resp = make_response(render_template('readcookie.html'))
    resp.set_cookie('userID', user)

    return resp
#'readcookie.html'包含指向另一个视图函数getcookie()的超链接，它读回并在浏览器中显示Cookie值。
@app.route('/getcookie')
def getcookie():
   name = request.cookies.get('userID')
   return '<h1>welcome '+name+'</h1>'


@app.route('/delCookie', methods=['GET'])
def delCookie():
    response = make_response('delCookie')
    response.delete_cookie('id')
    return response




if __name__=="__main__":
    app.run()
