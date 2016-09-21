import pickle

import requests

url = 'https://wordsapiv1.p.mashape.com/words/example'
headers = {'Accept': 'application/json', 'X-Mashape-Key': 'VydfqtWsTjmshakKVYTfiErs8NUVp1wFurMjsnu1okHoLDJGuL'}


def is_part_of_speech(word):
    return lambda x: x['partOfSpeech'] == word


# response = requests.get(url, headers=headers)
with open('response', 'rb') as f:
    response = pickle.load(f)
    filter(is_part_of_speech('noun'), [x for x in response.json()['results']])
