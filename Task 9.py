#Day 9

#Q1.Write a program to loop through a list of numbers and add +2 to every value to elements in list

list1=[2,4,6,8,10]
result=[]
for i in list1:
    result.append(i+2)
print(result)
#----------------------------------------------------------------------------------------------------

#Q2. Write a program to get the below pattern
54321
4321
321
21
1

for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end=' ')
    print()

#-----------------------------------------------------------------------------------------------------
 #Q3. Python Program to Print the Fibonacci sequence
def Fibonacci(n):
    if n < 0:
        print("Incorrect input")
 
    elif n == 1 or n == 2:
        return 1
 
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
    print(Fibonacci(11))
def fibo(n):
    n1, n2 = 0, 1
    count = 0
    if n<0:
        print("Incorrect Input")
    elif n == 1 or n == 2:
        print('1')
    else :
         while count < n:
                print(n1)
                nth = n1 + n2
                n1 = n2
                n2 = nth
                count += 1
fibo(9)
#--------------------------------------------------------------------------------------------------
#Q4. Explain Armstrong number and write a code with a function

num = int(input("Enter a number: "))
sum1 = 0
temp1 = num
while temp1 > 0:
    digit1 = temp1 % 10
    sum1 += digit1**3
    temp1 //= 10
if num == sum1:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")

#----------------------------------------------------------------------------------------------------
#Q5. Write a program to print the multiplication table of 9
for i in range(1,11):
    print("9 x ",i,' = ',i*9 )

#--------------------------------------------------------------------------------------------------
 #Q6. Check if a program is negative or positive
    lid=[-1,2,-45,50,-90,87]
for i in lid:
    if i >=0:
        print(i," is positive")
    else :
        print(i,' is negative ')

#-----------------------------------------------------------------------------------------------
#Q7. Write a program to convert the number of days to ages
def find( number_of_days ):
    year = int(number_of_days / 365)
    print(year,'Years ago !')
no_days=600
find(no_days)
#------------------------------------------------------------------------------------------------

#Q8.Solve Trigonometry problem using math function write a program to solve using math function
import math
def trigo(n,m):
    if n=='sin':
        return math.sin(m)
    elif n=='cos':
        return math.cos(m)
    elif n=='cosin':
        return math.cosine(m)
    elif n=='tan':
        return math.tan(m)
    elif n=='sec':
        return math.sec(m)
    elif n=='cosec':
        return math.cosec(m)
trigo('sin',90)

#-----------------------------------------------------------------------------------------
#Q9. create a basic calculator using if condition only

def calculate():
    print('+')
    print('-')
    print('*')
    print('/')
    print('%')
    print('**')
    operation = input("Select an operator:n")
    print("Enter two numbers")
    number_1 = int(input())
    number_2 = int(input())

    if operation == '+': # To add two numbers
        print(number_1 + number_2)
    elif operation == '-': # To subtract two numbers
        print(number_1 - number_2)
    elif operation == '*': # To multiply two numbers
        print(number_1 * number_2)
    elif operation == '/': # To divide two numbers
        print(number_1 / number_2)
    elif operation == '%': # To remainder two numbers
        print(number_1 % number_2)
    elif operation == '**': # To num1 exponent num2
        print(number_1 ** number_2)
    else:
        print('Invalid Input')
calculate()
#----------------------------------