import logging
from muffin_service.RSS_parser import RSSParser
from BeautifulSoup import BeautifulSoup
__author__ = 'ife'

class ProcessDomain():
    def __init__(self):
        pass

    def get_domain_details(self, html_content):
        rss_link = None

        try:
            soup = BeautifulSoup(html_content)
            title = soup.find('title')
            link = soup.find('link', type='application/rss+xml')
            if not link:
                logging.warning("URL has no RSS")
            rss_link = link.get('href')
        except Exception as ex:
            logging.warning(ex)
        return rss_link