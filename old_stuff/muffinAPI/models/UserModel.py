import bcrypt
from marshmallow import Schema
from marshmallow import fields
from werkzeug.security import generate_password_hash, check_password_hash
from muffinAPI.extensions import db
from muffinAPI.models.CRUD_Mixin import CRUD_MixIn

__author__ = 'ife'

class UserModel(db.Model, CRUD_MixIn):

    _id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    # password = db.String(db.String)
    _password = db.Column('password', db.String(255))
    email = db.Column(db.String(255)),
    _token = db.Column('token', db.String(255)),
    userId = db.Column(db.String(255)),
    provider = db.Column(db.String(255)),
    deviceId = db.Column(db.String(255))

    def _get_password(self):
        return self._password

    def _set_password(self, password):
        self._password = generate_password_hash(password,salt_length=20)

    def _set_token(self):
        self._token = bcrypt.gensalt()
    def _get_token(self):
        return self._token

    password = db.synonym('_password', descriptor=property(_get_password, _set_password))
    token = db.synonym('_token', description=property(_get_token, _set_token))

    def check_password(self,password):
        if self._password is None:
            return False
        return check_password_hash(self.password, password)

    def get_by_username(self, username):
        result = self.query.filter(db.text("username ='"+username+"'"))
        if result is None:
            return None
        else:
            return result

    def init(self, username=None, password=None, email=None, token=None, user_id=None, provider=None, device_id=None):
        self.username = username
        self.password = password
        self.email = email
        self.token = token
        self.user_id = user_id
        self.provider = provider
        self.deviceId = device_id


    @classmethod
    def authenticate(cls,username, password):
        user = cls.query.filter(UserModel.username == username).first()

        if user:
            authenticated = check_password_hash(password)
        else:
            authenticated = False
        return authenticated

class UserSchema(Schema):
    _id = fields.Integer()
    username = fields.String()
    _password = fields.String()
    email = fields.String()
    token = fields.String()
    userId = fields.String()
    provider = fields.String()
    deviceId = fields.String()

    def get_top_level_links(self, data, many):
        if many:
            self_link = "/user/"
        else:
            self_link = "/user/{}".format(data['_id'])
        return {'self': self_link}

    class Meta:
        type_ = 'user'




