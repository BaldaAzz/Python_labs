from urllib.parse import urlparse, urlunparse, urlsplit, urlunsplit


url = 'https://lpgenerator.ru/blog/2011/04/25/url-adresa-i-celevye-stranicy/'

result = urlparse(url)
result_tuple = tuple(result)

print(result.scheme)
print(result.netloc)
print(result.hostname)
print(result.port)
print(result.params)
print(result.query)
print(result.fragment )

print(urlunparse(result))
print()

url = 'ftp://user:123456@mysite.ru'

result = urlparse(url)

print(result.username)
print(result.password)

result = urlsplit(url)
print(result)
print(urlunsplit(result))
