#INHERITANCE
#1.single inheritance
#2.multilevel inheritance
#3.hierarchical inheritance
#4.multiple inheritance
#5.Hybrid inheritance
class A:
    name="reshma"
    age=20
class B(A):
    age=19
obj=B()
print(B.age)
print(B.name)

class A:
    name="reshma"
    age=20
class B(A):
    age=19
obj=B()
obj.name="reshu"
print(obj.age)
print(obj.name)

#multilevel inheritance
class Chairman:
    name="abc"
    age=70
    salary_details=[2000,3000,4000]
class Principal(Chairman):
    name="xyz"
    age=40
    student_details=[101,102,103]
class Faulty(Principal):
    name="pqr"
    age=35
obj=Faulty()
print(Faulty.student_details)
print(Principal.salary_details)

#hierarchical inheritance
class Father:
    height="tall"
    hair="black"
    color="fair"
class Child1(Father):
    name="child1"
class Child2(Father):
    name="child2"
print("inherited features of child1 are:")
obj=Child1()
print(obj.height)
print(obj.color)
print("inherited features of child2 are:")
obj1=Father()
print(obj1.hair)
print(obj1.color)

#diamond problem(occurs in multiple inheritance)

#multiple inheritance
class Father:
    height="tall"
    color="fair"
class Mother:
    height="short"
    color="white"
class Child(Father,Mother):
    name="abc"
print("features of child are:")
obj=Child()
print(obj.height)
print(obj.color)

#hybrid inheritance of hierarchical and multiple
class Vehicle:
    mileage="120cc"
    type="metal"
class body(Vehicle):
    type_of_body="black metal"
class tyre(Vehicle):
    no_of_tyres=2
class bike(body,tyre):
    bike_name="livo"
obj=bike()
obj1=body()
obj2=tyre()
print(obj1.type)
print(obj2.mileage)
print(obj.type_of_body)
print(obj.no_of_tyres)

class A:
    def method_1(self,a,b):
        print("sum of 2 numbers:",a+b)
class B(A):
    def method_1(self,a,b):
        print("mul of 2 numbers:",a*b)
obj=B()
obj.method_1(10,20)

