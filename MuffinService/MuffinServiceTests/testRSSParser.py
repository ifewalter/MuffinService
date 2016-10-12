__author__ = 'ife'
from MuffinService.RSSParser import RSSParser
import unittest


class testRSSParser(unittest.TestCase):

    def test_valid_page_url(self):
        url = 'http://example.com'
        rss = RSSParser(url)
        rss.get_url_content()
        self.assertIsNotNone(rss.get_url_content())


    def test_invalid_url(self):
        url = 'dsawdw://dfefwefd'
        rss = RSSParser(url)
        rss.get_url_content()
        self.assertIsNone(rss.get_url_content())



