import requests
#import json


def get_movies_title(id):
    url = 'https://ghibliapi.herokuapp.com/films/'
    r = requests.get(url)
    j = r.json()
    movie_index = j[id]
    movie_name = movie_index['title']
    print(movie_name)

if __name__ == "__main__":
    c = int(input("Ingrese el id de la película a consultar: "))
    get_movies_title(c)
