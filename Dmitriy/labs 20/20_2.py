from urllib.parse import urlparse,  urlunparse

url = 'http://www.user.by:50/test.php;st?var=10#metka'
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

print("url-адрес из отдельных значений:",urlunparse(tupleUrl)) 

print("url-адрес из geturl:",parsedUrl.geturl())

parsedFtp = urlparse(ftp)
print("Логин:", parsedFtp.username)
print("Пороль:", parsedFtp.password) 
