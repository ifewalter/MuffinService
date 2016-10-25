
import multiprocessing
import time
from db_things import DBThings
import builder

outqueue = None


class WorkerProcess(multiprocessing.Process):
    def __init__(self):
        multiprocessing.Process.__init__(self)
        self.exit = multiprocessing.Event()

    def doWork(self):
        global outqueue
        ob = outqueue.get()

        builder.crawl_url(ob)

    def run(self):
        while not self.exit.is_set():
            self.doWork()

    def shutdown(self):
        self.exit.set()

if __name__ == '__main__':
    global outqueue
    outqueue = multiprocessing.Queue()


    # creating the processes
    procs = []
    for x in range(50):
        procs.append(WorkerProcess())
        procs[x].start()

    #pass parameter to queue
    dbThings = DBThings()

    result = dbThings.get_domains_without_rss()
    if result:
        for url in result:
            outqueue.put(url)

    # outqueue.put(str(1))


    # # shutdown after 10 secs
    # time.sleep(10)
    # for p in procs:
    #     p.shutdown()

    # for p in procs:
    #     p.join()

    # try:
    #     while True:
    #         x = outqueue.get(False)
    #         print x
    # except:
    #     print "done"
