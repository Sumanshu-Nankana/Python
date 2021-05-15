import requests
import time

URL = 'https://httpbin.org/uuid'

def fetch(session, url):
    with session.get(url) as response:
        print(response.json()['uuid'])
        
def main():
    start = time.time()
    with requests.session() as session:
        for _ in range(100):
            fetch(session, URL)
    end = time.time()
    print(f"Total Time: {end - start}")
    
main()

# Took approx 15 seconds to hit 100 external requests