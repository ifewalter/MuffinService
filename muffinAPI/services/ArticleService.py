from marshmallow import Schema
from muffinAPI.models.ArticleModel import ArticleModel, ArticleSchema

__author__ = 'ife'

articleSchema = ArticleSchema(strict=True)

class ArticleService:
    def get_recent_articles(self, _limit):
        articleModel = ArticleModel()
        result = articleModel.get_latest_articles(_limit=10)
        return articleSchema.dump(result, many=True).data
