import time

__author__ = 'ife'

import newspaper
from crawler import Crawler
from db_things import DBThings

class Builder:
    def __init__(self):
        pass

    def build_urls(self,url):

        builder = newspaper.build(url)
        article_count = 0
        for article in builder.articles:
            dbthings = DBThings()
            url_processed = dbthings.check_url_exists(url)
            if article_count < 50:
                if url_processed is False:
                    # Avoid overloading client server
                    print "crawling"
                    self.crawl_url(article.url)
                    article_count += 1
        return
    def crawl_url(self,url):
        crawler = Crawler()
        crawler.prosess_content(url)
        return
