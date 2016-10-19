from flask import jsonify, request

from . import api
from .. import db
from rest_framework import status
from ..models.feeds_model import FeedsModel
from ..schemas.feeds import FeedsSchema


@api.route('/feeds', methods=['GET'])
def get_feeds():

    feeds_model = FeedsModel()
    top_feeds = feeds_model.get_latest(limit=10)
    feeds_schema = FeedsSchema(many=True).load(top_feeds)
    return feeds_schema.data, status.HTTP_200_OK




@api.route('/feed/<int:id>', methods=['GET'])
def get_feed(id):
    pass


@api.route('/feeds', methods=['POST'])
def create_feeds():
    pass


@api.route('/feeds/<int:id>', methods=['PUT'])
def update_feeds(id):
    pass


@api.route('/feeds/<int:id>', methods=['DELETE'])
def delete_feeds(id):
    pass
