# we will use multiprocessing library
# and can take advantage eof multiple cores of cpu
# and we will use Pool class
# One can create a pool of processes which will carry out tasks submitted to it with the Pool class.

import requests
import time
from multiprocessing.pool import Pool

URL = 'https://httpbin.org/uuid'

def fetch(session, url):
    with session.get(url) as response:
        print(response.json()['uuid'])
        
def main():
    start = time.time()
    with Pool() as pool:
        with requests.session() as session:
            pool.starmap(fetch, [(session, URL) for _ in range(100)])
    end = time.time()
    print(f"Total Time: {end - start}")
    
main()

# Took approx 5 seconds to hit 100 external requests
# So, it's much faster than synchrounous code
