import requests

posts = requests.get("https://jsonplaceholder.typicode.com/posts")
print(posts)