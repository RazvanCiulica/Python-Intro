import requests

def get_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    return response

print(get_posts().json())