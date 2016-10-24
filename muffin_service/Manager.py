from threading import Thread
import threading
import logging
from builder import Builder
from db_things import DBThings
from Queue import Queue

__author__ = 'ife'


class Manager(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue
        # super(Manager, self).__init__()

    def run(self):
        logging.debug("doing main work")
        url = self.queue.get()
        builder = Builder()
        builder.build_urls(url)

def start_work():
    dbthings = DBThings()

    result = dbthings.get_top_domains()
    queue = Queue()

    for url_item in result:
        worker = Manager(queue)
        worker.daemon=True
        worker.start()
        queue.put((url_item))
    queue.join()

    start_work()





