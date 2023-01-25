#language translator

from translate import Translator
obj=Translator(from_lang="english",to_lang="spanish")
new_name=obj.translate("sreeja")
print(new_name)

#method overloading
def m1(a,b):
     return(a+b)
def m1(a,b,c):
    return(a*b*c)
print(m1(10,20,30))

#method overriding
class A:
    def m1(self):
        return("in class A")
class B(A):
    def m1(self):
        return("in class B")
obj=B()
print(obj.m1())


#preventing method overriding
class Animal:
    def speak(self):
        return("animal speaks")
class Dog(Animal):
    def speak(self):
        return("dog barks")
class Cat(Animal):
    def speak(self):
        return("cat meows")
obj=Dog()
obj1=Cat()
print(obj1.speak())

#abstraction
from abc import ABC,abstractmethod
class Area(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
    @abstractmethod
    def calculate_circle_area(self):
        pass
class Square(Area):
    def calculate_area(self):
        print("in square method")
        pass
    def calculate_circle_area(self):
        pass
class Rectangle(Area):
     pass

obj=Square()
obj.calculate_area()

