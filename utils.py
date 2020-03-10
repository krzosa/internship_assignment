# funkcja do obliczenia odleglosci pomiedzy dwoma punktami geograficznymi
import geopy.distance

'''
inputs:  posts - wieksza lista obiektow zawierajaca joinKey(klucz obcy, w tym wypadku userId)
         users - mniejsza lista obiektow 
         joinKey - nazwa klucza na podstawie ktorego tabele mamy polaczyc
returns: mergedLists - polaczone ze soba listy obiektow posts i users
    posts i users powinny byc w relacji jeden do wielu

'''
def mergeLists(posts, users, joinKey):
    mergedLists = posts.copy()
    for i in range(len(posts)):
        for j in range(len(users)):
            if posts[i][joinKey] == users[j]['id']:
                for key in users[j].keys():
                    if key != "id":
                        mergedLists[i][key] = users[j][key]
    return mergedLists


'''
funkcja ktora oblicza ile kazdy z userow napisal postow

input:  userPosts - polaczone ze soba listy users i posts
returns:obiekt ktory wyglada: id1: [liczbaPostow, username],
                              id2: [liczbaPostow, username], ...
'''

def countPostsPerUser(userPosts):
    ids = {}
    for i in range(len(userPosts)):
        if userPosts[i]["userId"] not in ids:
            ids[userPosts[i]["userId"]] = [1, userPosts[i]["username"]]
        else:
            ids[userPosts[i]["userId"]][0]+=1

    return ids


# Funkcja ktora zwraca liste tytulow wszystkich postow.
def getPostTitles(posts):
    titles = []
    for i in range(len(posts)):
        titles.append(posts[i]['title'])
    return titles


'''
Oblicza macierz odleglosci - kazdy uzytkownik jak daleko ma od kazdego uzytkownika
input:   lista z informacjami o uzytkownikach
returns: macierz odleglosci np.        user1   user2
                                user1  0       Z km
                                user2  Y km    0
'''
def calculateDistances(users):
    neighbours = {}
    rng = range(len(users))
    for i in rng:
        tempDistance = 0
        neighbours[i] = []
        # GEO1 = LATITUDE, LONGTITUDE
        geo1 = (users[i]['address']['geo']['lat'], users[i]['address']['geo']['lng'])
        for j in rng:
            geo2 = (users[j]['address']['geo']['lat'], users[j]['address']['geo']['lng'])
            distance = geopy.distance.distance(geo1, geo2).km
            neighbours[i].append(distance)
    return neighbours
        

'''
Szuka najblizszych sasiadow w macierzy odleglosci
input:   macierz odleglosci
returns: np. {user1: [najblizszyUser, dystans],
              user2: [najblizszyUser, dystans],
              ... }
'''
def findNearestNeighbours(usersDistances):
    for key,value in usersDistances.items():
        nearest = min(i for i in value if i > 0)
        usersDistances[key] = [value.index(nearest), nearest]
    return usersDistances