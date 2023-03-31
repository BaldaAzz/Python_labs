'''
1.	Определите статус запроса следующих адресов:
https://ru.wikipedia.org/wiki/%D0%A1%TTP#410
https://www.pageranker.ru/articles/troubleshooting/167--403-forbidden.htm
https://python-scripts.com/reqsts
http://avgrodno.by/raspisanie/
https://mail.yandex.by/?uid
2.	Напишите программу, которая информирует пользователя об успешном выполнении выше представленных запроса.
3.	Получите содержимое запросов в байтах.
4.	Конвертируйте полученную информацию в строку.
5.	Выведите информацию об HTTP заголовков
'''
import requests


urls = {
    'https://ru.wikipedia.org/wiki/%D0%A1%TTP#410': None,
    'https://www.pageranker.ru/articles/troubleshooting/167--403-forbidden.htm': None,
    'https://python-scripts.com/reqsts': None,
    'http://avgrodno.by/raspisanie/': None,
    'https://mail.yandex.by/?uid': None
}


for key in urls.keys():
    urls[key] = requests.get(key).status_code
    if urls[key] == 200:
        print(f'Успешно выполнен! \n{key}')
    else:
        print(f'Ответ на запрос: {urls[key]}')
    bytes_reqest = str(bytes(urls[key]))
    print(bytes_reqest)
    response = requests.get(key)
    print('Информация об HTTP заголовков',response.headers, '\n\n')
