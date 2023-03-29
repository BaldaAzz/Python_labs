""" def content(func):
    def wrapper(text):
        
        for all in text:
            print(' <p>\n  ', end='')
            func(all)
            print(' </p>')
    return wrapper

@content
def text_content(text):
    print(' ', text, '\n', end='')

a = []
n = 1

while (i := input(f'Глава {n}\n')) != '':
    a.append(i)
    n += 1
    
text_content(a) """

def title(func):
    def wrapper(text):
        print('<h1>\n', end='')
        func(text)
        print('</h1>')
    return wrapper

def content(func):
    def wrapper(text):
        for all in text:
            print(' <p>\n  ', end='')
            func(all)
            print(' </p>')
    return wrapper

def container(func):
    def wrapper(text):
        print('<div>\n', end='')
        func(text)
        print('</div>')
    return wrapper

@title
@container
@content
def text_content(text):
    print(' ',text, '\n', end='')

a = []
n = 1

while (i := input(f'Глава {n}\n')) != '':
    a.append(i)
    n += 1
    
text_content(a)