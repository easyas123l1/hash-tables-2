"""
Caching web client

Go get URLs
Cache the result

Cache entries should timeout after 10 seconds 

Things to do:
* Read data from URLs
* Have a CacheEntry object to hold data and timestamps
* Compute time differences against timestamps
* REPL that reads URLs and prints the result data
"""
import urllib.request
import time


class CacheEntry:
    def __init__(self, url, data):
        self.url = url
        self.data = data
        self.timestamp = time.time()


cache = {}
CACHE_TIMEOUT_SECONDS = 10


def get_data(url):
    curtime = time.time()

    if url not in cache or curtime-cache[url].timestamp > CACHE_TIMEOUT_SECONDS:
        with urllib.request.urlopen(url) as f:
            data = f.read().decode('utf-8', "ignore")
            cache[url] = CacheEntry(url, data)
    else:
        age = curtime - cache[url].timestamp
        print(f"Age: {age}")

    return cache[url]


def main():
    while True:
        url = input("Enter URL: ")

        entry = get_data(url)

        print(entry.data[:80])


if __name__ == "__main__":
    main()
