from _ast import Raise
import logging
import requests.exceptions
from MuffinService import config

__author__ = 'ife'


class RSSParser():
    page_url = None
    page_content = None

    page_url_exception = "Invalid page URL"

    def __init__(self, _page_url):
        self.page_url = _page_url


    def get_url_content(self):
        content = None
        try:
            request_result = requests.get(self.page_url, headers=config.REQUEST_HEADERS)
            content = request_result.text
        except requests.exceptions.MissingSchema as missingSchemaException:
            logging.warning(missingSchemaException)
            #TODO: Explicitly handle other exceptions
        except:
            logging.warning("Failed to get content")

        return content

    def extract_rss_from_html(self, html_content):
        pass