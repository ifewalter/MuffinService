# -*- coding: utf-8 -*-
import pprint

from flask import Blueprint, current_app, request, jsonify
from muffinAPI.models.ArticleModel import ArticleModel
from muffinAPI.models.UserModel import UserSchema, UserModel
from muffinAPI.services.ArticleService import ArticleService
from muffinAPI.services.UserService import UserService

user_api = Blueprint('user', __name__, url_prefix='/user')
userSchema = UserSchema(strict=True)

@user_api.route('/', methods=['POST'])
def create_user():
    raw_dict = request.get_json(force=True)

    userSchema.validate(raw_dict)
    request_dict = raw_dict['data']['attributes']
    userService = UserService()
    userService.create_user(request_dict['username'],request_dict['password'],request_dict['email'],request_dict[''],request_dict[''],request_dict[''],request_dict[''])

    user_result = userService.get_by_username(request_dict['username'])
    results = userSchema.dump(user_result).data
    return results, 200
