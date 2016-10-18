from MuffinSchema.BaseModel import BaseModel
from MuffinWeb.muffin import db

from flask_security.core import RoleMixin

__author__ = 'ife'


class RolesModel(BaseModel, RoleMixin):
    __tablename__ = 'auth_role'
    name = db.Column(db.String(80), nullable=False, unique=True)
    description = db.Column(db.String(255))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Role %r>' % self.name