from .. import db
from .base_model import BaseModel


class UserCategoriesModel(BaseModel):

    __tablename__ = 'user_categories'
    user_id = db.Column(db.Integer)
    category_id = db.Column(db.Integer)


    def update_user_categories(self, user_id, categories_list):
        for category in categories_list:
            self.update_user_category(user_id=user_id, category_id=category)

    def update_user_category(self, user_id, category_id):
        self.user_id = user_id
        self.category_id = category_id
        self.save()

    def delete_user_categories(self, user_id):
        self.query.filter(db.text('user_id = '+user_id)).delete()
        return

    def get_user_categories(self, user_id):
        result = self.query.filter(db.text("user_id = '"+user_id+"'")).all()
        return result

    def __repr__(self):
        return 'Category Users {}>'.format(self.id)
