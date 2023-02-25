from urllib.parse import urlparse
import  requests

links = ["https://translate.yandex.by/fro=tabbar",
        "https://www.youtube.com/watch?v=34",
        " http://docs.google.com/spreadshe/",
        "https://python-scripts.com/reqsts",
        "http://avgrodno.by/raspisanie/"]

for i in links:
    response = requests.get(i)
    parsedUrl = urlparse(i) 
    print("/////////////////////////////////////////////////\n",i)
    print(response.status_code)
    
    info = { "Протокол:" : parsedUrl.scheme,
             "Порт:": parsedUrl.port,
             "Путь:" : parsedUrl.path,
             "Параметры:" : parsedUrl.params,
             "Cтрока запроса:" : parsedUrl.query,
             "Якорь:": parsedUrl.fragment,
             }
    
    for j in info:
        if info[j]:
            print(j,info[j])
        else:
            print(j,"Not definded")
            
    text = response.content.decode('UTF-8') 
    print(response.headers) 
    