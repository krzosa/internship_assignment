""" 
Wariant 2
Stwórz program/skrypt który
● pobierze dane o postach z ​https://jsonplaceholder.typicode.com/posts​ ​i połączy je z danymi o
userach ​https://jsonplaceholder.typicode.com/users
● policzy ile postów napisali userzy i zwróci listę stringów w postaci “​user_name napisał(a) ​count 
postów”
● sprawdzi czy tytuły postów są unikalne i zwróci listę tytułów które nie są.
● dla każdego użytkownika znajdzie innego użytkownika, który mieszka najbliżej niego
Pożądanym elementem danego rozwiązania jest także zestaw testów sprawdzających jego poprawność.
"""
import requests


def merge_lists(posts, users, joinKey):
    mergedLists = posts
    for i in range(len(posts)):
        for j in range(len(users)):
            if posts[i][joinKey] == users[j]['id']:
                for key in users[j].keys():
                    if key != "id":
                        mergedLists[i][key] = users[j][key]
    return mergedLists


def countUsersPosts(userPosts):
    pass


reqUsers = requests.get("https://jsonplaceholder.typicode.com/users")
reqPosts = requests.get("https://jsonplaceholder.typicode.com/posts")
if [reqUsers.status_code, reqPosts.status_code] != [200, 200]: 
    raise Exception("Error: couldn't retrieve data from the server")

posts = reqPosts.json()
users = reqUsers.json()
userPosts = merge_lists(posts, users, "userId")