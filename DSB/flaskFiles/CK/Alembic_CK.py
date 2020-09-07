# -*- coding:utf-8 -*-

##################数据库迁移############################

#1》manager.py添加：
    # migrate = Migrate(main.app, models.db)
    # manager.add_command("db", MigrateCommand)

#1》 python manage.py db
    #ython manage.py db init

#3》开始第一次跟踪
    #python manage.py db migrate -m "Initial migration"

#4》将记录文件应用到数据库中(实时升级数据库结构)
    #python manage.py db upgrade

#5》回滚到某一个记录环境中
    #python manage.py db history
    #python manage.py db downgrade <history_id>
