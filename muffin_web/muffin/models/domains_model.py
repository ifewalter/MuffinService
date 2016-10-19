from .. import db
from .base_model import BaseModel


class DomainsModel(BaseModel):

    __tablename__='domains'
    name = db.Column(db.String(255), nullable=True)
    url = db.Column(db.String(255))
    has_rss = db.Column(db.Boolean, default=False)
    favicon = db.Column(db.String(255), nullable=True)
    feeds = db.relationship('FeedsModel', backref=db.backref('domains',lazy='joined'), lazy='dynamic')

    def __repr__(self):
        return 'Domain {}>'.format(self.id)
