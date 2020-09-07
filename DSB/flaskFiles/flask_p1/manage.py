# -*- coding:utf-8 -*-
from flask_script import Manager, Server
from app_v1 import app
from app_v1 import models
from flask_migrate import MigrateCommand, Migrate


# Init manager object via app object
manager = Manager(app)
# Create some new commands
manager.add_command("server", Server())


#版本控制
migrate = Migrate(app, models.db)
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
                Post=models.Post)

if __name__ == '__main__':
    manager.run()


