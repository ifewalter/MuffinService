from .. import ma
from ..models.feeds_model import FeedsModel


class FeedsSchema(ma.ModelSchema):

    class Meta:
        model = FeedsModel


feeds_schema = FeedsSchema()
feeds_schema = FeedsSchema(many=True)
