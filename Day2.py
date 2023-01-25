#lists and operations on lists
l=[1,2,3]
print(l.remove(1))
#extend
a=[10,20,30,40]
b=[100,200,300]
a.extend(b)
print(a)
#count
l=[1,1,1,1,2,2,2,2]
print(l.count(2))

a=[10,20,30]
b=a
b[0]=100
print(a)
#copy
a=[10,20,30]
b=a.copy()
b[0]=100
print(a)
#reverse list
a=[10,20,30]
b=a.sort(reverse=True)
print(a)
#sort
a=[5,1,7]
a.sort()
print(a)
#sorted
a=[3,1,2]
b=sorted(a)
print("b=",b)
print("a=",a)
#type conversion
#implicit and explicit
#string to integer
a=list('12345')
print(a)
b=list(map(int,a))
print(b)

a=list(input("enter numbers"))
print(a*2)


#conditional statements
#if statement
num=int(input())
if num%2==0:
    print("even")
#if else statement
num=int(input())
if ((num/2)*2)==num:
    print("even")
else:
    print("odd")
#if and elif
choice_day_num=int(input())
if choice_day_num==1:
    print("monday")
elif choice_day_num==2:
    print("tuesday")
elif choice_day_num==3:
    print("wednesday")
elif choice_day_num==4:
    print("thursday")
elif choice_day_num==5:
    print("friday")
elif choice_day_num==6:
    print("saturday")
elif choice_day_num==7:
    print("sunday")
else:
    print("invalid choice")


#loops
#for loop
l=[1,2,3,4]
for i in l:
    print(i**2)
#while loop
i = 1
while i < 6:
  print(i)
  i += 1


#find the index at which the given number is present
l=[88,11,77,66,99,22]
r=55
temp=False
for i in range(len(l)):
    if l[i]==r :
        print(i)
        temp=True
        break
if temp==False:
    print("element not found")

#list comprehension + condition satisfying
l=[x for x in range(0,51) if x%2==0]
print(l)
#another way
l=[x for x in range(1,101) if x%7==0 and x%11==0]
print(l)

#**********************************************list input *********************************************************************
#sum of given list (indivisual sum of positive numbers and negative numbers)
a=list(map(int,input().split()))
p,n=0,0
for i in a:
    if i<0:
        n+=i
    else:
        p+=i
print(p+n)
#dictionaries
l=[]
d={}
d.update({'user1':'pass1'})
d.update({'user2':'pass2'})
d.update({'user3':'pass3'})
l.append(d)
print(l)

#checking username and password in dictionary(login system)
l=[{'reshma123':'passresh'},{'reshma1305':'passreshma1305'},{'reshu11':'passreshu'},{'reshma2003':'passreshma2003'}]
username=input()
password=input()
temp={username:password}
if temp in l:
          print("found")
else:
    print("not found")

