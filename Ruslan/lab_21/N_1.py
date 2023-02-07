import requests


urls = {
    'https://ru.wikipedia.org/wiki/%D0%A1%TTP#410': None,
    'https://www.pageranker.ru/articles/troubleshooting/167--403-forbidden.htm': None,
    'https://python-scripts.com/reqsts': None,
    'http://avgrodno.by/raspisanie/': None,
    'https://mail.yandex.by/?uid': None
}


for key in urls.keys():
    urls[key] = requests.get(key)
    if urls[key] == 200:
        print(f'Успешно выполнен! \n{key}')
    else:
        print(f'Ответ на запрос: {urls[key].status_code}')

    response = urls[key]
    print('Информация об HTTP заголовков',response.headers, '\n\n')
    print() # !!!НЕхватает вывода запроса в байтовом виде

