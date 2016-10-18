from _ast import Raise
import logging
from BeautifulSoup import BeautifulSoup
import requests.exceptions
from muffin_service import config

__author__ = 'ife'


class RSSParser():
    page_url = None
    page_content = None

    page_url_exception = "Invalid page URL"


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

    def extract_rss_link_from_html(self, html_content):
        rss_link = None

        try:
            soup = BeautifulSoup(html_content)
            link = soup.find('link', type='application/rss+xml')
            if not link:
                logging.warning("URL has no RSS")
            rss_link = link.get('href')
        except Exception as ex:
            logging.warning(ex)
        return rss_link