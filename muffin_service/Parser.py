import urlparse

__author__ = 'ife'

import requests
from BeautifulSoup import BeautifulSoup, Comment
import html2text



class Parser:
    href_links = []

    def __init__(self):
        pass

    def get_data(self, url):
        data = requests.get(url).text
        return data.encode('utf-8')

    def extract_links(self, data, domain):
        soup = BeautifulSoup(data.decode('utf-8'))
        for anchor_link in soup.findAll('a', href=True):
            if self.is_valid_protocol(anchor_link):
                self.href_links.append(anchor_link['href'])
            else:
                self.href_links.append(urlparse.urljoin(domain, anchor_link['href']))
            print anchor_link['href']
        return self.href_links


    def is_valid_protocol(self,url):
        if str(url).startswith("http"):
            return True
        return False

    def sanitize(self, data):
        soup = BeautifulSoup(data)
        for element in soup.findAll(['script', 'style']):
            element.extract()
        for comments in soup.findAll(text=lambda text: isinstance(text, Comment)):
            comments.extract()
        return html2text.html2text(soup.getText())



# parser = Parser()
# data = parser.get_data("http://lindaikejisblog.com/")
# # print data
# print parser.extract_links(data=data, domain="http://lindaikejisblog.com/")
# print parser.sanitize(data=data)
