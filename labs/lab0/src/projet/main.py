class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b
    

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Person):
            return False
        return self.name == value.name and self.age == value.age

    def get_name(self):
        return self.name
    
    def fn_statique():
        return "Je suis une fonction statique"
