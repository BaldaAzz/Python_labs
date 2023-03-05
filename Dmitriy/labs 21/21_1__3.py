import  requests

yandex =  'https://translate.yandex.by/fro=tabbar'
vk = 'https://vk.com/dev'
google ='http://docs.google.com/spreadshe/'
python_scripts = 'https://python-scripts.com/reqsts'
avagrodno = 'http://avgrodno.by/raspisanie/'

links = {'https://translate.yandex.by/fro=tabbar':requests.get(yandex).status_code,
        'https://vk.com/dev':requests.get(vk).status_code,
        ' http://docs.google.com/spreadshe/':requests.get(google).status_code,
        'https://python-scripts.com/reqsts':requests.get(python_scripts).status_code,
        'http://avgrodno.by/raspisanie/':requests.get(avagrodno).status_code
        }

state = { 
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
for link in links:
    response = requests.get(link)     
    for status in state:
        if int(links[link]) == status:
            print("/////////////////////\n",link, links[link], state[status],"\n//////////////////////////////////")
            response_in_str = response.content.decode('UTF-8')
            print(response.headers)
            