import requests
from pprint import pprint

url = "https://jsonplaceholder.typicode.com/posts/1"

def get_posts(url):
    try:
        response = requests.get(url)
        print(response, dir(response), type(response))
        return response
    except Exception as e:
        raise Exception(f"Error occurred during get operation")


if __name__ == "__main__":
    response = get_posts(url)
    print(f"Status Code : {response.status_code}")
    pprint(response.json())