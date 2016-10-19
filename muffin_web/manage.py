#! /usr/bin/env python

import os

from flask_compress import Compress
from flask_cors import CORS
from flask_script import Manager

from muffin import create_app, db


app = create_app(os.getenv('MUFFIN_CONFIG', 'testing'))
CORS(app)
Compress(app)
manager = Manager(app)


@manager.shell
def make_shell_context():
    return dict(app=app, db=db)


if __name__ == '__main__':
    manager.run()