import time

__author__ = 'ife'

import newspaper
from Crawler import Crawler
from DBThings import DBThings

class Builder:
    def __init__(self):
        pass

    def build_urls(self,url):

        builder = newspaper.build(url)

        print url
        print "building"

        print len(builder.articles)

        article_count = 0

        for article in builder.articles:
            dbthings = DBThings()
            url_processed = dbthings.check_url_exists(url)
            if article_count < 50:
                if url_processed is False:
                    # Avoid overloading client server
                    time.sleep(2)
                    print "crawling"
                    self.crawl_url(article.url)
                    # Avoid overloading client server

                    # Commented out for, Performance concerns
                    # time.sleep(2)
                    # self.build_urls(article.url)
                    article_count += 1
        return

    def crawl_url(self,url):
        crawler = Crawler()
        crawler.prosess_content(url)
        return
