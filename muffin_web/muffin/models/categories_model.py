from .. import db
from .base_model import BaseModel


class CategoriesModel(BaseModel):

    __tablename__= 'categories'
    name = db.Column(db.String(255))
    feeds = db.relationship('FeedsModel', backref=db.backref('categories', lazy='joined'), lazy='dynamic')

    def __repr__(self):
        return 'Category {}>'.format(self.id)
