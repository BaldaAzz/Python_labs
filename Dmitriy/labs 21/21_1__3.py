import  requests

links = ["https://translate.yandex.by/fro=tabbar",
        "https://kinogo.by/21789-the-addams-family_2019.htm",
        " http://docs.google.com/spreadshe/",
        "https://python-scripts.com/reqsts",
        "http://avgrodno.by/raspisanie/"]

for i in links:
    print("//////////////////////////////////////////////////////////////////////////////////////////////", i)
    try:
        response = requests.get(i)
        print(response.status_code)
        
        text = response.content.decode('UTF-8') 
        print(response.headers) 
    except:
        print("Ошибка")
    
   
