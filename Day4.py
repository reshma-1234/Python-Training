#OBJECT ORIENTED PROGRAMMING
#class
#class variables
#class methods
#self(means 'this' in java)
#constructor (def __init__(self) )
class Student:
    student_name="no name"
    def __init__(self,name):
        print("object  created")
        print(name)
        print(self.student_name)
s1=Student("reshma")

class Student:
    student_name="no name"
    def __init__(self,name):
        self.student_name=name
        print(self.student_name)
s1=Student("reshma")

class Student:
    student_name="no name"
    def __init__(self,name):
        self.student_name=name
s1=Student("reshma")
s2=Student("lakshmi")
s3=Student("mogalapu")
print(s1.student_name)

#updating name which is not recommended because it directly may access the data base
class Student:
    student_name="no name"
    def __init__(self,name):
        self.student_name=name
    def update_name(self,new_name):
        pass
s1=Student("reshma")
s2=Student("lakshmi")
s3=Student("mogalapu")
s1.student_name="new_name"
print(s1.student_name)

class Student:
    student_name="no name"
    def __init__(self,name):
        self.student_name=name
    def update_name(self,new_name):
        self.student_name=new_name
s1=Student("reshma")
s2=Student("lakshmi")
s3=Student("mogalapu")
print(s1.student_name)
s1.update_name("reshu")
print(s1.student_name)

# to make private keep 2 underscores to the variable to make it secure
# the  private variables are not accessible outside the class

N=int(input())
arr=[]
for i in range(N):
        operation=input().split()
        if operation[0]=='add':
              arr.append(int(operation[1]))
        elif operation[0]=='insert':
                ele=int(operation[1])
                ind=int(operation[2])
                arr.insert(ind,ele)
        elif operation[0]=='print':
             if len(arr)!=0:
                    print(arr)
        elif operation[0]== 'remove':
                    ele=int(operation[1])
                    if ele in arr:
                        arr.remove(ele)
        elif operation[0]=='pop':
              if len(arr)>0:
                     arr.pop()

        else:
             print("Invalid Input")



