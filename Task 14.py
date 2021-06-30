#list down Error
#Name error
list = 12
print(list1)

#---------------------------x---------------------------------------------x----------------------------------------
#TYpeError
a = '123'
a+= 123
#---------------------------x---------------------------------------------x-----------------------------------------
#TypeError
l = [1,2,3,4,5,6]
for i in range(2,1):
    print(i+1)

#---------------------------x---------------------------------------------x----------------------------------------
#syntax Error
for i range(1,10):
    print(i)
#---------------------------x--------------------------------------------x-----------------------------------------
#index error
l = [1,2,3.4,5,56,7]
for i in range(len(l)):
    print(l[i+1])
#----------------------------x---------------------------------------------x----------------------------------------

#module not fount error
import modulexyz

#----------------------------x--------------------------------------------------x---------------------------------
#design a simple calculator using try and except
def calculate():
    try:
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
    except Exception as e:
        print(e)

#------------------------------------------------------------------------------------------------------------------
#print one message if try block raises a nameError and another for other error
try:
    a = 123
    if a==123:
        print(b)
        raise NameError("Name error")
    if a >0:
        raise ValueError("Value error")
except NameError as ne:
        print(ne)
except ValueError as ve:
    pritn(ve)

#----------------------------------------------------------------------------------------------------------------------
#when try - except scenario is not required?
#python Exception are error scenarios that alter the normal execution flow of the program the process of the code inside the elseblock is executed if there are no exception raised

#------------------------------------------------------------------------------------------------------------------
#try getting an input inside try catch block
try:
    age=int(input('Enter your age: '))
except:
    print ('You have entered an invalid