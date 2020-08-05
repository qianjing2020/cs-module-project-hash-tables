
"""
Have a input loop that gets a url from user
Fetch the data at the url and display it
Create a cache or lookup table
"""
import urllib.request
import datetime
class CacheEntry:
    def __init__(self, url, data):
        self.url = url
        self.data = data
        self.timestamp = get_timestamp()

cache = {}
def get_timestamp():
    return datetime.datetime.now().timestamp()

def get_data(url):
    # current time
    cur_time = get_timestamp()
    # if url not exist or it is older than 10 sec
    if url not in cache or cur_time-cache[url].timestamp > 10:
        print("Cache miss!")
        resp = urllib.request.urlopen(url)
        # get data as byte string
        data = resp.read()        
        resp.close()        
        # store in cache as CacheEntry
        cache[url] = CacheEntry(url, data)
    print(cache[url].timestamp)
    return cache[url].data

if __name__=='__main__':
    while True:
        url = input("enter an url:")
        print(get_data(url)[:100])
