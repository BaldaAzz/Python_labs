from urllib.parse import urlparse
import  requests

urls = {
    'https://ru.wikipedia.org/wiki/%D0%A1%TTP#410': {'status_code': '', 'parse': {'scheme':'', 'netloc':'', 'path':'', 'params':'', 'query':'', 'fragment':''}},
    'https://www.pageranker.ru/articles/troubleshooting/167--403-forbidden.htm': {'status_code': '', 'parse': {'scheme':'', 'netloc':'', 'path':'', 'params':'', 'query':'', 'fragment':''}},
    'http://avgrodno.by/raspisanie/': {'status_code': '', 'parse': {'scheme':'', 'netloc':'', 'path':'', 'params':'', 'query':'', 'fragment':''}},
    'https://mail.yandex.by/?uid': {'status_code': '', 'parse': {'scheme':'', 'netloc':'', 'path':'', 'params':'', 'query':'', 'fragment':''}}
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
    urls[url]['status_code'] =( response := requests.get(url)).status_code
    url_parse = urlparse(url)
    urls[url]['parse']['scheme'] = i if (i:=url_parse.scheme) != '' else print('нету протокола')
    urls[url]['parse']['netloc'] = i if (i:=url_parse.netloc) != '' else print('нету схемы')
    urls[url]['parse']['path'] = i if (i:=url_parse.path) != '' else print('нету пути')
    urls[url]['parse']['params'] = i if (i:=url_parse.params) != '' else print('нету параметров')
    urls[url]['parse']['query'] = i if (i:=url_parse.query) != '' else print('нету строки')
    urls[url]['parse']['fragment'] = i if (i:=url_parse.fragment) != '' else print('нету якоря')
    
    print(url)
    print(status_codes[urls[url]['status_code']])
    print(urls[url],'\n')
           



""" Сделайте разбор URL-адреса 5-ти интернет-адресов и определите статус запроса.
Выведите информацию пользователю об элементах URL-адресов. 
Напишите программу, которая информирует пользователя об отсутствии элементов при разборе URL-адреса. 
Выведите информацию пользователю о статусе кода запроса адресов.
Выполните сбор интернет-адресов с помощью двух функций и получите информацию в байтах, затем конвертируйте в строку.
 """