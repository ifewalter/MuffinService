from flask import jsonify, request

from . import api
from rest_framework import status



@api.route('/user/auth/', methods=['POST'])
def authenticate_user():
    pass