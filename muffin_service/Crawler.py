from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

import time
from .Classifier import Classifier
from DBThings import DBThings

from . import articleDateExtractor


__author__ = 'ife'

from newspaper import Article
from .Parser import Parser



from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
# from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.summarizers.lex_rank import LexRankSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words


class Crawler:

    authors = ''
    keywords = ''

    def __init__(self):
        pass
    def prosess_content(self,url):
        article = Article(url)

        article.download()
        # article.html
        article.parse()

        dbthings = DBThings()
        parser = Parser()

        if article.authors:
            self.authors = ','.join(map(str, article.authors))
        if article.keywords:
            self.keywords = ','.join(map(str, article.keywords))


        publish_date = articleDateExtractor.extractArticlePublishedDate(article.url)
        # time.sleep(5)

        parser = HtmlParser.from_url(url, Tokenizer('english'))
        # or for plain text files
        # parser = PlaintextParser.from_file("document.txt", Tokenizer(LANGUAGE))
        stemmer = Stemmer('english')

        summarizer = Summarizer(stemmer)
        summarizer.stop_words = get_stop_words('english')

        all_sentences = ''

        for sentence in summarizer(parser.document, 10):
            all_sentences += sentence._text # print(sentence)#all_sentence = all_sentence + sentence

        # TODO: Pay for better license to speed up this process
        # time.sleep(80)
        # classifier = Classifier()
        # category = classifier.classify_news(data=all_sentences)
        category = 'General'


        if publish_date is not None:
            dbthings.insert_extracted(self.authors, str(publish_date), all_sentences.encode('utf-8','ignore') ,article.top_image, self.keywords, article.url, article.title, category)
        return


