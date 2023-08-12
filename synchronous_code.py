# Synchronous Code

import requests
import time

number_of_requests = 50
url = "https://jsonplaceholder.typicode.com/posts/"


def fetch_posts(post_num):
    post_url = url + str(post_num)
    print(f"Hitting Get Request for {post_num} Post")
    response = requests.get(post_url)
    return response.text

if __name__ == "__main__":
    start_time = time.time()

    for i in range(1, number_of_requests+1):
        response = fetch_posts(i)

    end_time = time.time()

    print(f"Synchronous Execution Time: {end_time - start_time}")