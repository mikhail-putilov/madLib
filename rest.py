import pickle

import requests

url = 'https://wordsapiv1.p.mashape.com/words/{}/definitions'
url_rhyme = 'https://wordsapiv1.p.mashape.com/words/{}/rhymes'
headers = {'Accept': 'application/json', 'X-Mashape-Key': 'VydfqtWsTjmshakKVYTfiErs8NUVp1wFurMjsnu1okHoLDJGuL'}


def _has_mark_of_part_of_speech(word):
    return lambda x: x['partOfSpeech'] == word


def ask_rhyme(word):
    response = requests.get(url_rhyme.format(word), headers=headers)
    rhymes = [x for x in response.json()['rhymes']['all']]
    for i, rhyme_word in enumerate(rhymes):
        result_dict = {}
        response_about_rhyme_word = requests.get(url.format(rhyme_word), headers=headers)
        definitions = [x for x in response_about_rhyme_word.json()['definitions']]
        for definition in definitions:
            parts_of_speech = result_dict.setdefault(rhyme_word, set())
            parts_of_speech.add(definition['partOfSpeech'])
        yield result_dict


def is_part_of_speech(definitions, part_of_speech):
    return len(list(filter(_has_mark_of_part_of_speech(part_of_speech), definitions))) > 0


rhymes = ask_rhyme("hello")
for i, info in enumerate(rhymes):
    if i < 2:
        print(i, info)
    else:
        break
