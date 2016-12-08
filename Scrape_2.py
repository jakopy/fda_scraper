import os
import Queue
import threading
import requests

class Downloader(threading.Thread):

    def __init__(self,queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            url = self.queue.get()
            self.download_file(url)
            self.queue.task_done()
    def download_file(self, url):
        filename = url.split("&&&")[1]
        filename = "data_scrape_2/" + filename + ".txt"
        url = url.split("&&&")[0]
        response = requests.get(url)
        data = response.text
        with open(filename,'wb') as f:
            f.write(data.encode('utf-8'))
        f.close()
            
def main(urls):
    queue = Queue.Queue()
    for i in range(90):
        t = Downloader(queue)
        t.setDaemon(True)
        t.start()

    for url in urls:
        queue.put(url)

    queue.join()

def get_new_pages(return_type):
    filename = "drugs_set_ids.txt"
    with open(filename,"r") as f:
        data = f.readlines()
    count = 0
    set_ids = []
    for i in data:
        set_ids.append(i.replace("\n",""))
    return set_ids


def page_range(the_range,newpages):
    url = "https://dailymed.nlm.nih.gov/dailymed/services/v2/spls/{}.xml"
    start = the_range[0]
    end = the_range[1]
    url_list = []
    for i in range(start,end,1):
        url_list.append(url.format(newpages[i])+"&&&Page_"+str(i))
    return url_list

if __name__ == "__main__":
    import time
    t = time.time()
    print "start time is %f" % (t)
    try:
        the_range = [57000,58000]
        newpages = get_new_pages("setid")
        urls = page_range(the_range,newpages)
        main(urls)
        print "the total time was: %f" % (time.time()-t)
    except Exception as e:
        print e
        print "the total time was: %f" % (time.time()-t)
    print "the total time was: %f" % (time.time()-t)
