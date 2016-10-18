#! /usr/bin/env python

import os

from flask_compress import Compress
from flask_cors import CORS
from flask_script import Manager
from flask_security import SQLAlchemyUserDatastore, Security

from MuffinWeb.muffin.schemas.RolesModel import RolesModel
from MuffinWeb.muffin.models import UsersModel
from muffin import create_app, db

app = create_app(os.getenv('MUFFIN_CONFIG', 'default'))
CORS(app)
Compress(app)
manager = Manager(app)


user_datastore = SQLAlchemyUserDatastore(db, UsersModel, RolesModel)
security = Security(app, user_datastore)

@manager.shell
def make_shell_context():
    return dict(app=app, db=db)


if __name__ == '__main__':
    manager.run()
