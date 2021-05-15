# Instead of processes, we will use Threads
# Threads are light weights, as compare to process
# But because of GIL, we can run one thread at a time
# But because of context-switching, still it faster than synchrounous code

# we will use ThreadPoolExecutor


import requests
import time
from concurrent.futures import ThreadPoolExecutor

URL = 'https://httpbin.org/uuid'

def fetch(session, url):
    with session.get(url) as response:
        print(response.json()['uuid'])
        
def main():
    start = time.time()
    with ThreadPoolExecutor(max_workers=10) as executor:
        with requests.session() as session:
            executor.map(fetch, [session]*100, [URL]*100)
            executor.shutdown(wait=True)
    end = time.time()
    print(f"Total Time: {end - start}")
    
main()

# It tooks only 1.5 seconds ; even fater than multiprocessing
# Till will even decreases if we use max_workers = 20

# because in multiprocessing - there are overhead of creating a process
# also a portion of work still happening sequence, because it depends on number of processes
# so if we have 4 processes so work divided ammong 4, but it will done sequentialy