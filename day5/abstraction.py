from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def eat(self):
        pass

    def sleep(self):
        return "I am sleeping"


class Dog(Animal):

    def eat(self):
        return "Dog is eating"


d = Dog()

print(d.eat())
print(d.sleep())