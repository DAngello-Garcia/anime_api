from django.shortcuts import render
import requests


def movies_titles(request):
    url = 'https://ghibliapi.herokuapp.com/films/'
    r = requests.get(url)
    j = r.json()
    return render(request, 'titles_view.html', {'films': j})

