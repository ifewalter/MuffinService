from .. import ma
from ..models.domains_model import DomainsModel


class DomainsSchema(ma.ModelSchema):

    class Meta:
        model = DomainsModel


domains_schema = DomainsSchema()
domains_schema = DomainsSchema(many=True)
