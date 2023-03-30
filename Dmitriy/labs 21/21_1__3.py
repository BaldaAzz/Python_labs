import requests

links = {
    'https://ru.wikipedia.org/wiki/%D0%A1%TTP#410': {'status_code': 'Uknown'},
    'https://www.pageranker.ru/articles/troubleshooting/167--403-forbidden.htm': {'status_code': 'Uknown'},
    'http://avgrodno.by/raspisanie/': {'status_code': 'Uknown'},
    'https://mail.yandex.by/?uid': {'status_code': 'Uknown'}
}

status = { 
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

for link in links.keys():
    links[link]['status_code'] = requests.get(link).status_code
    print(link, '\nстатус:', status[links[link]['status_code']], links[link]['status_code'])
    response = requests.get(link)
    response_in_str = response.content.decode('UTF-8')
    print("Информация об заголовках", response.headers.keys())
            