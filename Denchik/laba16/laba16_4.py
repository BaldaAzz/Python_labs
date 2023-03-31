def title(func):
    def wrapper(text):
        print('<h1>\n', end='')
        func(text)
        print('</h1>')
    return wrapper

def content(func):
    def wrapper(text):
        print(' <p>\n  ', end='')
        func(text)
        print(' </p>')
    return wrapper

def container(func):
    def wrapper(text):
        print('<div>\n', end='')
        func(text)
        print('</div>')
    return wrapper

print('А)')
@title
def text_content(text):
    print(' ',text, '\n', end='')

text_content('Личные данные')

print('\nБ)')

@container
@content
def text_content(text):
    print(' ',text, '\n', end='')

text_content('Ваше имя:')

