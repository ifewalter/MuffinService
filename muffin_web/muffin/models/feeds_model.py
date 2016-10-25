from .. import db
from .base_model import BaseModel
from ..models.user_categories_model import UserCategoriesModel


class FeedsModel(BaseModel):

    __tablename__='feeds'

    author = db.Column(db.String(255))
    domain_id = db.Column(db.Integer, db.ForeignKey('domains.id'))
    publish_date = db.Column(db.String(255))
    content = db.Column(db.Text)
    top_image = db.Column(db.String(255))
    keywords = db.Column(db.String(255))
    url = db.Column(db.String(255))
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    title = db.Column(db.String(255))


    def get_user_latest(self, user_id, limit=10):
        user_categories = UserCategoriesModel()
        user_categories_result = user_categories.get_user_categories()
        if user_categories_result is None:
            return None
        query = "select * from 'feeds' where "+ " or ".join("'id' = " + str(cat_id) for cat_id in user_categories_result.id)
        result = db.engine.execute(query)
        if result is None:
            return None
        # untested
        return result


    def get_latest(self, limit=10):
        result = self.query.order_by('publish_date desc').limit(limit)
        if result:
            return result
        return None



    def __repr__(self):
        return 'Feeds {}>'.format(self.id)
