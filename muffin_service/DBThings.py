import threading
import MySQLdb
import MySQLdb.cursors
import itertools

class DBThings():

    def __init__(self):
        # self.lock = threading.Lock()
        pass

    def check_url_exists(self,url):
        # self.lock.acquire()
        db = MySQLdb.connect("localhost","root",">Predict?","summer")

        cursor = db.cursor()

        cursor.execute("select url from articles where url = '"+MySQLdb.escape_string(url)+"'")

        if cursor.rowcount > 0:
            db.close()
            return True
        db.close()
        # self.lock.release()
        return False

    def check_title_exists(self, title):
        pass

    def insert_extracted(self, author, publish_date, text, top_image, keywords, url, title, category):
        # self.lock.acquire()
        try:
            db = MySQLdb.connect("localhost","root",">Predict?","summer")
            cursor = db.cursor()
            cursor.execute("insert into articles (author, publish_date, content, top_image, keywords,url, title, category)values ('"+MySQLdb.escape_string(author)+"','"+publish_date+"','"+MySQLdb.escape_string(text.decode('utf-8','ignore'))+"','"+top_image+"','"+keywords+"','"+url+"','"+MySQLdb.escape_string(title)+"','"+category+"')")
            db.commit()
            db.close()
        except Exception as e:
            print e.message

        # self.lock.release()
        return

    def get_top_domains(self):
        # self.lock.acquire()
        db = MySQLdb.connect("localhost","root",">Predict?","summer")
        cursor = db.cursor()
        cursor.execute("select url from domains")
        url_list = list(itertools.chain.from_iterable(cursor))
        db.close()
        # self.lock.release()
        return url_list

