from .. import ma
from marshmallow import fields, Schema
from ..models.categories_model import CategoriesModel


class CategoriesSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()
    created_at = fields.String()
    modified_at = fields.String()

    class Meta:
        _type = 'feeds'

    # self links
    def get_top_level_links(self, data, many):
        if many:
            self_link = "/categories/"
        else:
            self_link = "/category/{}".format(data['id'])
        return {'self': self_link}



