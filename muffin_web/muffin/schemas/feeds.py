from .. import ma
from marshmallow import validate
from marshmallow_sqlalchemy.fields import fields
from ..models.feeds_model import FeedsModel


class FeedsSchema(ma.ModelSchema):

    not_blanks = validate.Length(min=1, error='Field cannot be blank')
    id = fields.Integer(dump_only=True)
    author = fields.String()
    domain_id = fields.Integer()
    publish_date = fields.String()
    content = fields.String()
    top_image = fields.String()
    keywords = fields.String()
    url = fields.String()
    category_id = fields.Integer()
    title = fields.String()


    class Meta:
        # model = FeedsModel
        _type = 'feeds'

    # self links
    def get_top_level_links(self, data, many):
        if many:
            self_link = "/feeds/"
        else:
            self_link = "/feed/{}".format(data['id'])
        return {'self': self_link}



