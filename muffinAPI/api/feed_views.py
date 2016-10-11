# -*- coding: utf-8 -*-
import json
import pprint

from flask import Blueprint, current_app, request, jsonify
from muffinAPI.models.ArticleModel import ArticleModel
from muffinAPI.services.ArticleService import ArticleService

api = Blueprint('feed', __name__, url_prefix='/feed')


@api.route('/recent', methods=['GET'])
def get_feeds():

    article = ArticleService()
    result = article.get_recent_articles(_limit=10)
    response = jsonify(article=result)
    response.status_code = 200
    return response
