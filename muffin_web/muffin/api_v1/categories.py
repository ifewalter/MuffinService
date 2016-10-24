from flask import jsonify, request

from . import api
from rest_framework import status
from ..models.categories_model import CategoriesModel
from ..schemas.categories import CategoriesSchema

categories_schema = CategoriesSchema()

@api.route('/categories', methods=['GET'])
def get_categories():
    categories_model = CategoriesModel()
    result = categories_model.get_all()
    return jsonify(categories_schema.dump(result, many=True).data), status.HTTP_200_OK
