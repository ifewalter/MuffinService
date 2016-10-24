import logging
from muffin_service.RSS_parser import RSSParser
from BeautifulSoup import BeautifulSoup
__author__ = 'ife'

class ProcessDomain():
    def __init__(self):
        pass

    def get_domain_details(self, html_content):
        rss_link = None
        title = None
        favicon = None
        soup = BeautifulSoup(html_content)
        try:
            title = soup.find('title')

        except Exception as ex:
            logging.warning(ex)

        try:
            link = soup.find('link', type='application/rss+xml')
            if not link:
                logging.warning("URL has no RSS")
                rss_link = link.get('href')

        except Exception as ex:
            logging.warning(ex)
        try:
            favicon_link = soup.find('link', rel='shortcut icon')
            favicon = favicon_link.get('href')
        except Exception as ex:
            logging.warning(ex)

        return rss_link, title, favicon
