# -*- coding:utf-8 -*-
'''
    初始化Flask初始化脚本
'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#加载配置文件
app.config.from_object('config')

#数据库迁移
db = SQLAlchemy(app)

from app_v1 import views, models