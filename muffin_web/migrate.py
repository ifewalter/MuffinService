import os
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager
from muffin_web.muffin import create_app, db

__author__ = 'ife'

app = create_app(os.getenv('MUFFIN_CONFIG', 'development'))
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()