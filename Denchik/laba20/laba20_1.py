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

result = urlparse(urls[1])

print('Имя пользователя:', result.username)
print('Пороль:', result.password)

print()

for all in urls:
    urls_split = urlsplit(all)
    print(urls_split)
    print(urlunsplit(urls_split))
    print()