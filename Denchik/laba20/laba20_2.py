from urllib.parse import urlparse, urlunparse, urlsplit, urlunsplit


url = 'http://www.user.by:50/test.php;st?var=10#metka'

result = urlparse(url)

print('Название протокола:',result.scheme)
print('Название домена:', result.hostname)
print('Номер порта:', result.port)
print('Путь:', result.path)
print('Параметры:', result.params)
print('Строка запроса:', result.query)
print('Якорь:', result.fragment)
print()
print(urlunparse(result))
print()
print('Имя пользователя:', result.username)
print('Пороль:', result.password)