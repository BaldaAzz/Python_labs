def title(fn):
    def wrapper(text):
        print("<h1>")
        fn(text)
        print("</h1>")
    return wrapper

text = str(input("Введите текст:"))

@title
def text_content(text):
    print(text)

text_content(text)


