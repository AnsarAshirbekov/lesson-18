# Напишите программу, в которой есть главный класс с текстовым полем. В главное классе
# должен быть метод для присваивания значения полю: без аргументов и с одним текстовым
# аргументом. Объект главного класса создаётся передачей одного текстового аргумента
# конструктору. На основе главного класса создается класса потомок. В классе-потомке нужно
# добавить числовое поле. У конструктора класса-потомка два аргумента.

# Реализуйте старый алгоритм с использованием
# полиморфизма.

# Чтобы продемонстрировать работу полиморфизма, создадим внутри наших классов два полиморфных метода, которые будут 
# называться одинаково, но будут работать по-разному в зависимости от класса

class MainClass:
    def __init__(self):
        self.text = ''
    
    def set_text(self):
        self.text = input('Введите любой текст: ')

    def get_text(self):
        return self.text
    
    def info(self):
        return f"MainClass: Text - {self.text}" # здесь метод будем выводить значение только атрибута текста

class ChildClass(MainClass):
    def __init__(self):
        super().__init__()  
        
        self.number = 0 
    
    def set_number(self):
        self.number = int(input('Введите любое число: '))
    
    def get_number(self):
        return self.number
    
    def info(self):
        return f"ChildClass: Text - {self.text}, Number - {self.number}" # а здесь значения текста и числа


child_object = ChildClass()

child_object.set_text()
child_object.set_number()
print(child_object.get_text())
print(child_object.get_number())

print(child_object.info()) # так как объект принадлежит дочернему классу, значит он будет выводить то, что прописано
# в методе этого класса