from . import api
from flask import jsonify, request
from rest_framework import status
from ..models.user_categories_model import UserCategoriesModel
from ..common.helpers import token_required
from ..schemas.user_categories import UserCategoriesSchema

__author__ = 'ife'

schema = UserCategoriesSchema(strict=True)

@api.route('/user/categories/', methods=['GET'])
@token_required
def get_user_categories():
    user_categories_model = UserCategoriesModel()
    result = user_categories_model.get_all()
    return jsonify(schema.dump(result).data), status.HTTP_200_OK

"""
update user categories.
receives PUT request with data format
    categories:[1,2,3,4,5...]

"""
@api.route('/user/categories/', methods=['PUT'])
@token_required
def update_user_categories():
    input_dict = request.get_json(force=True)
    # TODO: get userId from token header
    user_id = None
    user_categories_model = UserCategoriesModel()
    user_categories_model.update_user_categories(user_id, input_dict['categories'])
    return '', status.HTTP_200_OK
