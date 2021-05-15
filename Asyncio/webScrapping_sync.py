import time
import requests

def download_file(url):
    print(f"Started Downloading {url}")
    response = requests.get(url)
    print(f"Finished Downloading {url}")
    return response.content

def write_file(n, content):
    filename = f'sites/sync_{n}.html'
    with open(filename, 'wb') as f:
        print(f"Started writing {filename}")
        f.write(content)
        print(f"Finished writing {filename}")
        
        
        
if __name__ == "__main__":
    t = time.perf_counter()
    for n, url in enumerate(open('urls.txt').readlines()):
        content = download_file(url)
        write_file(n, content)
    t2 = time.perf_counter() - t
    print(f"Total time taken: {t2:0.2f} seconds")
    
# It took approx 19 seconds
    