#arrays
#matrix addition
arr1=[]
arr2=[]
arr=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    element=[]
    for j in range(3):
        element.append((int(input("enter element:"))))
    arr1.append(element)
print(arr1)
for i in range(3):
    element=[]
    for j in range(3):
        element.append((int(input("enter element:"))))
    arr2.append(element)
print(arr2)
for i in range(3):
    for j in range(len(arr1[0])):
        arr[i][j]=arr1[i][j]+arr2[i][j]
print("the sum is:")
print(arr)
#transpose of matrix
X = [[12,7],
    [4 ,5],
    [3 ,8]]
result = [[0,0,0],
         [0,0,0]]
# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[j][i] = X[i][j]
for r in result:
   print(r)

#string methods
#captilize
#title
#lower
#upper
#count
#split
#join
#isdigit
#isdecimal
#isaplha
#isalnum
#swapcase

#string formating
num=3.14
print("the square of {} is {:.2f}".format(num,num*num))
#another way
num=3.14
print(f"the square of {num} is {num*num:.5f}")

#simple calculator program
operand1=int(input())
operand2=int(input())
choice_of_operation=input()
if choice_of_operation=='+':
    print(operand1+operand2)
elif choice_of_operation=='-':
    print(operand1-operand2)
elif choice_of_operation=='*':
    print(operand1*operand2)
elif choice_of_operation=='/':
    try:
        print(operand1/operand2)
    except:
        print("operand2 cannot be zero")
else:
    print("invalid choice")

#exception handling
try:
    arr=list(map(int,input().split(' ')))
    print(arr)
except:
    print("enter integer input")

#eval function
print(eval("1+3/5*9//10"))
#functions
#types of functions
#1.regular functions
#2.default value functions
#3.keyword argument function
#4.variable length function
#prime   number
def checking_prime(num):
    flag=0
    for i in range(2,num):
        if num%i==0:
            flag=1
            break
    if flag==1:
        print("not prime")
    else:
        print("prime")
num=int(input())
checking_prime(num)
#according to efficiency there are 4 ways to write code
#xor operation
print(5^10)
#shift operation
print(7<<3)
