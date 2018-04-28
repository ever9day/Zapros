import requests


key = 'trnsl.1.1.20180428T041518Z.e3c7043ba832dcdb.effb407761138b7605cff0d2a5a7ba312c058ef0'

n = input('1 Рус \n 2 Англ \n 3 Испанский: ')

if n == '1':
    n = 'ru'
if n =='2':
    n = 'en'
if n == '3':
    n = 'es'


n1 = input('1 Рус \n 2 Англ \n 3 Испанский: ')

if n1 == '1':
    n1 = 'ru'
if n1 =='2':
    n1 = 'en'
if n1 == '3':
    n1 = 'es'
        

data = {'key' : key,
        'text': input(' '),
        'lang' : n +'-'+ n1,
        'format' : 'plain'}

answer = requests.post('https://translate.yandex.net/api/v1.5/tr.json/translate', data = data)

dictAnswer = answer.json()

print(dictAnswer['text'])
