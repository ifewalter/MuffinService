from flask import jsonify, request

from . import api
from .. import db
from rest_framework import status
from ..models.feeds_model import FeedsModel
from ..common import helpers
from ..schemas.feeds import FeedsSchema

feeds_schema = FeedsSchema(strict=True)

@api.route('/feeds/', methods=['GET'])
def get_feeds():
    feeds_model = FeedsModel()
    user_id = helpers.get_user_id_from_header_token()
    if user_id is 0:
        top_feeds = feeds_model.get_latest(limit=10)
    else:
        top_feeds = feeds_model.get_user_latest(user_id=user_id, limit=10)

    return jsonify(feeds_schema.dump(top_feeds, many=True).data), status.HTTP_200_OK

@api.route('/feed/<int:id>/', methods=['GET'])
def get_feed(id):
    pass