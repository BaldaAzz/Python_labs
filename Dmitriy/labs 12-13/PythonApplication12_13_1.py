class Strings(): 
    
    def __init__(self,designer):
        self.designer = designer
   
    def spaseing(self):
        count = 0
        for i in  self.designer:
            if i == ' ':
                count += 1
        return(count)

    def replace(self):
        return(str.lower(self.designer))
    
text = Strings(designer= str(input('Введите текст:')))

print("колличество пробелов:",text.spaseing())
print("текст в нижнем регистре:",text.replace())
