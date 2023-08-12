import requests
import time
import multiprocessing

number_of_requests = 50
url = "https://jsonplaceholder.typicode.com/posts/"

def fetch_posts(post_num):
    post_url = url + str(post_num)
    print(f"Hitting Get Request for {post_num} Post")
    response = requests.get(post_url)
    return response.text

if __name__ == "__main__":
    start_time = time.time()

    processes = []
    for i in range(1, number_of_requests+1):
        process = multiprocessing.Process(target=fetch_posts, args=(i,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    end_time = time.time()

    print(f"Multiprocessing Execution Time: {end_time - start_time}")
