# -*- coding:utf-8 -*-
from flask_script import Manager, Server
from app_v1 import app
from app_v1 import models
##管理数据库结构
from flask_migrate import Migrate, MigrateCommand



# Init manager object via app object
manager = Manager(app)


#管理数据库结构
# Init migrate object via app and db object
migrate = Migrate(app, models.db)

# Create some new commands
manager.add_command("server", Server())


#管理数据库结构
manager.add_command("db", MigrateCommand)



@manager.shell
def make_shell_context():
    """Create a python CLI.

    return: Default import object
    type: `Dict`
    """
    return dict(app=app,
                db=models.db,
                User=models.User,
                Post=models.Post,
                Comment=models.Comment,
                Tag=models.Tag,
                posts_tags=models.posts_tags)

if __name__ == '__main__':
    manager.run()



