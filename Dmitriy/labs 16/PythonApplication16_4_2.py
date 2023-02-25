def content(fn):
    def wrapper(text):
        print("<div>")
        fn(text)
        print("</div>")
    return wrapper 

def container (fn):
    def wrapper(text):
        print("<p>")
        fn(text)
        print("</p>")
    return wrapper

text = str(input("Введите текст:"))

@content
@container
def text_content(text):
    print(text)

text_content(text)

