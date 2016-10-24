import os

from flask_compress import Compress
from flask_cors import CORS
from flask_script import Manager

from muffin import create_app, db


app = create_app(os.getenv('MUFFIN_CONFIG', 'development'))
# CORS(app)
Compress(app)
manager = Manager(app)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,token')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response


@manager.shell
def make_shell_context():
    return dict(app=app, db=db)


if __name__ == '__main__':
    manager.run()
