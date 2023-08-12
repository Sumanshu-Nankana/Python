# Multithreading Code

import requests
import time
import threading

number_of_requests = 50
url = "https://jsonplaceholder.typicode.com/posts/"

def fetch_posts(post_num):
    post_url = url + str(post_num)
    print(f"Hitting Get Request for {post_num} Post")
    response = requests.get(post_url)
    return response.text

if __name__ == "__main__":
    start_time = time.time()
    threads = []
    for i in range(1, number_of_requests+1):
        thread = threading.Thread(target=fetch_posts, args=(i,))
        threads.append(thread)
        thread.start()

    #waiting for threads to finish
    for thread in threads:
        thread.join()

    end_time = time.time()

    print(f"Multithreading Execution Time: {end_time - start_time}")