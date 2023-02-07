from urllib.parse import urlparse, urlunparse


url = 'http://www.user.by:50/test.php;st?var=10#metka'

result = urlparse(url)
result_typle = tuple(result)

print(result)
print(result.scheme)
print(result.hostname)
print(result.port)
print(result.path)
print(result.query)
print(result.fragment)

print(urlunparse(result))

print(result.username)
print(result.password)