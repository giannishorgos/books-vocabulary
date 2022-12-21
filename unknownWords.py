import requests


def saveToFile(word, meaning):
    with open('vocabulary.txt', 'a') as file:
        file.write('{} : {}\n'.format(word, meaning))
        file.write('===================================\n\n')


def get_meaning(word):
    try:
        response = requests.get(
            'https://api.dictionaryapi.dev/api/v2/entries/en/{}'.format(word))
        data = response.json()
        meaning = data[0].get('meanings')[0].get(
            'definitions')[0].get('definition')
        return meaning
    except:
        return -1


while True:
    word = input("Give word: ")
    meaning = get_meaning(word)
    print(meaning)
    if meaning != -1:
        saveToFile(word, meaning)
