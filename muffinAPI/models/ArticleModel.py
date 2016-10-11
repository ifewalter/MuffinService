from marshmallow import Schema, fields
from muffinAPI.extensions import db
__author__ = 'ife'



class ArticleModel(db.Model):

    __tablename__ = 'articles'

    _id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(255))
    domain = db.Column(db.Integer)
    publish_date = db.Column(db.String(255))
    content = db.Column(db.Text)
    top_image = db.Column(db.String(255))
    keywords = db.Column(db.String(255))
    url = db.Column(db.String(255))
    category = db.Column(db.String(255))
    title = db.Column(db.String(255))

    def get_latest_articles(self, _limit = 10, _id = 0):
        result = self.query.filter(db.text("_id > "+str(_id))).order_by('DATE(publish_date) desc').limit(_limit)
        return result

class ArticleSchema(Schema):
    _id = fields.Integer()
    author = fields.String()
    domain = fields.String()
    publish_date = fields.String()
    content = fields.String()
    top_image = fields.String()
    keywords = fields.String()
    url = fields.String()
    category = fields.String()
    title = fields.String()

    def get_top_level_links(self, data, many):
        if many:
            self_link = "/articles/"
        else:
            self_link = "/articles/{}".format(data['_id'])
        return {'self': self_link}

    class Meta:
        type_ = 'articles'

