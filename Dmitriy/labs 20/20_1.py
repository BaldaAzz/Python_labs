from urllib.parse import urlparse, urlsplit, urlunparse, urlunsplit

url = "https://lpgenerator.ru/blog/2011/04/25/url-adresa-i-celevye-stranicy"
ftp = "ftp://user:123456@mysite.ru"

parsedUrl = urlparse(url) 

tupleUrl = tuple(parsedUrl) 

print("Протокол:", parsedUrl.scheme) 

print("Домен:", parsedUrl.netloc) 

print("Порт:", parsedUrl.port) 

print("Путь:", parsedUrl.path) 

print("Параметры:", parsedUrl.params) 

print("строка запроса:", parsedUrl.query) 

print("Якорь:", parsedUrl.fragment) 

urlunparse(tupleUrl) 

parsedFtp = urlparse(ftp)
print("Логин:", parsedFtp.username)
print("Пороль:", parsedFtp.password) 

splitedUrl = urlsplit(url)
splitedFtp = urlsplit(ftp) 

collectedUrl = urlunsplit(splitedUrl)
collectedFtp = urlunsplit(splitedFtp) 
