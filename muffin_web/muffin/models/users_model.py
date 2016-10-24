import logging
from flask.ext.security import SQLAlchemyUserDatastore, Security

from flask_security.core import UserMixin
# from muffin_web.manage import app

from muffin_web.muffin import db
from muffin_web.muffin.common.helpers import generate_token
from muffin_web.muffin.models.base_model import BaseModel
from muffin_web.muffin.models.roles_model import RolesModel
from muffin_web.muffin.models.roles_users_model import roles_users
from muffin_web.muffin.common import helpers

__author__ = 'ife'


class UsersModel(BaseModel, UserMixin):
    __tablename__ = 'auth_user'
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    # Why 45 characters for IP Address ?
    # See http://stackoverflow.com/questions/166132/maximum-length-of-the-textual-representation-of-an-ipv6-address/166157#166157
    last_login_ip = db.Column(db.String(45))
    current_login_ip = db.Column(db.String(45))
    login_count = db.Column(db.Integer)
    token = db.Column(db.String(30))
    roles = db.relationship('RolesModel', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

    def create_user(self):

        if self.email is None or self.password is None:
            logging.warning('Email and Password cannot be null')
            return None
        try:
            SQLAlchemyUserDatastore(db, UsersModel, RolesModel).create_user(email=self.email, password=self.password,
                                       first_name=self.first_name, last_name=self.last_name, token=generate_token(),
                                       active=self.active)
            db.session.commit()
            return self
        except Exception as ex:
            logging.warning(ex)

    def get_id_by_token(self, token):
        result = self.query.filter(db.text("token= '"+token+"'")).first()
        if result:
            return result.id

    def __repr__(self):
        return '<User %r>' % self.email
