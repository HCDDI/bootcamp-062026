from abc import ABC
class Animal(ABC):
    def eat():
        pass
    def sleep(self):
        return "i am sleeping"
class Dog(Animal):
    def eat(self):
        return "i am eating dog food"