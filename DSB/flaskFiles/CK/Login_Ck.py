# -*- coding:utf-8 -*-

from flask_login import login_user, logout_user, current_user, login_required


#1> login_user:     注册这个有效的登录，我们调用 Flask-Login 的 login_user 函数。

#2>logout_user:     登出

#3> current_user:       局变量 current_user 是被 Flask-Login 设置的，登录成功之后可以用current_user来取该用户的其他属性，这些属性都是sql语句查来并赋值给对象的

#4>login_required:      添加了 login_required 装饰器。这确保了这页只被已经登录的用户看到。






