from marshmallow import Schema
from marshmallow_sqlalchemy.fields import fields

__author__ = 'ife'


class UserCategoriesSchema(Schema):

    id = fields.Integer(dump_only=True)
    category_id = fields.Integer()


    class Meta:
        _type = 'feeds'

    # self links
    def get_top_level_links(self, data, many):
        if many:
            self_link = "/categories/user"
        else:
            self_link = "/category/user{}".format(data['id'])
        return {'self': self_link}




