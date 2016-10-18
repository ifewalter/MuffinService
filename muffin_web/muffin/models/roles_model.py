from flask_security.core import RoleMixin

from muffin_web.muffin import db
from muffin_web.muffin.models import base_model

__author__ = 'ife'


class RolesModel(base_model, RoleMixin):
    __tablename__ = 'auth_role'
    name = db.Column(db.String(80), nullable=False, unique=True)
    description = db.Column(db.String(255))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Role %r>' % self.name