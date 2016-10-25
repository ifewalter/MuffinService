import time
from manager import outqueue

__author__ = 'ife'

import newspaper
from crawler import Crawler
from db_things import DBThings


def crawl_url(url):
    crawler = Crawler()
    crawler.prosess_content(url)
    return


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
                    time.sleep(2)
                    print "crawling"
                    outqueue.put(article.url)
                    article_count += 1
        return
