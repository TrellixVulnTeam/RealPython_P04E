import requests
import json

def index():
    return dict()

def grab_movies():
    session.m = []
    YOUR_OWN_KEY = 'nfbz7r6mm8rfqmzkrzyawv6v'
    url = requests.get("http://api.rottentomatoes.com/api/public/v1.0/lists/movies/in_theaters.json?apikey={}".format(YOUR_OWN_KEY))
    binary = url.content
    output = json.loads(binary)
    movies = output['movies']
    for movie in movies:
        session.m.append(pulse(movie["title"]))
    session.m.sort()
    return TABLE(*[TR(v) for v in session.m]).xml()

def pulse(movie):
    text = movie.replace('_', ' ')
    url = 'http://text-processing.com/api/sentiment/'
    data = {'text': text}
    r = requests.post(url, data=data)
    binary = r.content
    output = json.loads(binary)
    label = output["label"]
    pos = output["probability"]["pos"]
    neg = output["probability"]["neg"]
    neutral = output["probability"]["neutral"]
    return text, label, pos, neg, neutral
