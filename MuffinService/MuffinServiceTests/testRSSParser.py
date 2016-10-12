__author__ = 'ife'
from MuffinService.RSSParser import RSSParser
import unittest


class testRSSParser(unittest.TestCase):



    def test_valid_page_url(self):
        url = 'http://example.com'
        rss = RSSParser()
        rss.page_url = url
        rss.get_url_content()
        self.assertIsNotNone(rss.get_url_content())

    def test_invalid_url(self):
        url = 'dsawdw://dfefwefd'
        rss = RSSParser()
        rss.page_url = url
        rss.get_url_content()
        self.assertIsNone(rss.get_url_content())

    def test_valid_extract_rss_link_from_html(self):
        rss = RSSParser()
        content ='<html><head><link rel="alternate" type="application/rss+xml" title="Punch Newspapers &raquo; Feed" href="http://punchng.com/feed/"/>' \
                   '<link rel="alternate" type="application/rss+xml" title="Punch Newspapers &raquo; Comments Feed" href="http://punchng.com/comments/feed/"/>' \
                   '<link rel="alternate" type="application/rss+xml" title="Punch Newspapers &raquo; Punch Newspapers &#8211; Nigeria news, news in Africa, politics,' \
                   ' Entertainment, Sports Comments Feed" href="http://punchng.com/punch-newspapers-read-newspaper-nigeria/feed/"/></head><body></body></html>'

        link = rss.extract_rss_link_from_html(html_content=content)
        self.assertEqual(link, 'http://punchng.com/feed/')


    def test_no_rss_link_from_null_html(self):
        rss =RSSParser()
        content = ''
        link = rss.extract_rss_link_from_html(content)
        self.assertEqual(link, None)


