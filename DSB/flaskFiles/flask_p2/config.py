# -*- coding:utf-8 -*-


#表单配置
CSRF_ENABLED = True     #激活 跨站点请求伪造 保护
SECRET_KEY = 'you-will-never-guess'     #建立一个加密的令牌


OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]



SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@192.168.2.8:3306/ods'  #数据库信息
SQLALCHEMY_TRACK_MODIFICATIONS = True
