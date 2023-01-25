#datatypes and arithmetic operatotrs
a=1
print(type(a))
b=1.00
print(type(b))
c="abbbbbbbbbbbbbbbccccccccc"
d="""this is used
for the documents purpose"""
e=[1,2,3,[4,5,6]]
print(e[3][1])
l=[1,2,3,(70,80,60)]
print(l)
print(l[3][1])
t=(1,2,3,[4,5,6])
print(t)
print(l[3][1])
s={1,2,3}
print(type(s))
f=a+b
print(f)
g=b-a
print(g)

#operators in python
a%=82
print(a)
print(1&64)
print(64 or 16)
#membership operators (in , not in)
list = [1, 2, 3, 4, 5 ]
if 2 in list:
    print("2 is present")
if 10 not in list:
    print("10 not present")
#identity operators(is and is not)
a = 20
b = 20
if ( a is b ):
   print "Line 1 - a and b have same identity"
else:
   print "Line 1 - a and b do not have same identity"


#ternary operator:- syntax: (condition)?True_part:False_part

#ternary operator is if else in python . syntax:if (condition) true_part else (condition)
a, b = 10, 20
min = a if a < b else b
print(min)

