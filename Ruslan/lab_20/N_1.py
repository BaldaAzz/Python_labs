from urllib.parse import urlparse, urlunparse, urlsplit, urlunsplit


urls = ('https://lpgenerator.ru/blog/2011/04/25/url-adresa-i-celevye-stranicy/',
        'ftp://user:123456@mysite.ru')

result = urlparse(urls[0])

print('Название протокола:',result.scheme)
print('Название домена:', result.hostname)
print('Номер порта:', result.port)
print('Путь:', result.path)
print('Якорь:', result.fragment)

print(urlunparse(result))
print()


url = 'ftp://user:123456@mysite.ru'

result = urlparse(url)

print('Имя пользователя:', result.username)
print('Пороль:', result.password)

# result = urlsplit(url)
# print(result)
# print(urlunsplit(result))
