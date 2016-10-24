import json
import requests

__author__ = 'ife'

class Classifier:

    def __init__(self):
        pass

    def classify_news(self,data):
        json_data = {'texts':[data]}

        post_result = requests.post('https://api.uclassify.com/v1/mvazquez/news-classifier/classify',headers={"Authorization":"Token 4Jbq5gLe5qjF"}, json=json_data)

        post_json = json.loads(post_result.text)

        highest_index = 0
        highest_point = 0

        for i,val in enumerate(post_json[0]['classification']):
            if highest_point < (val['p'] * 100):
                highest_index = i
                highest_point = (val['p'] * 100)
        return post_json[0]['classification'][highest_index]['className']
