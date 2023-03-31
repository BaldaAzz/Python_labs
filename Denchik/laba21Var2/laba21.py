import requests

urls = {
    'https://ru.wikipedia.org/wiki/%D0%A1%TTP#410': {'status_code': 'Uknown'},
    'https://www.pageranker.ru/articles/troubleshooting/167--403-forbidden.htm': {'status_code': 'Uknown'},
    'http://avgrodno.by/raspisanie/': {'status_code' : 'Uknown'},
    'https://mail.yandex.by/?uid': {'status_code': 'Uknown'}
}

status_codes = { 
    102 : 'Processing',
    200 : 'Ok',
    204 : 'No Content',
    400 : 'Bad Request',
    403 : 'Forbidden',
    404 : 'Not Found',
    408 : 'Request Timeout',
    410 : 'Gone',
    500 : 'Internal Server Error',
    521 : 'Web Server Is Down',
    522 : 'Connection Timed Out',
    524 : 'A timeout Occurred'
    } 

for url in urls.keys():
    urls[url]['status_code'] = requests.get(url).status_code
    print(url,'\n status:' ,status_codes[urls[url]['status_code']])
    response = requests.get(url)
    print('Информация об HTTP заголовков',response.headers, '\n\n')
