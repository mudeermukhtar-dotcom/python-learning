#Write a Python program to create a function named greet() that prints Hello Mudeer when the function is called.
'''def greet():
 print("hello mudeer")
greet()'''
#Write a Python program to create a function named square() that prints the square of 5.
'''def square(a):
    result=a*a
    print(result)
square(5)'''
#Write a Python program to create a function named add() that adds two numbers and prints their sum.
'''def add(a,b):
    sum=a+b
    print(sum)
add(2,3)'''



#Write a Python program to create a function named multiply() that takes two numbers as arguments and prints their multiplication.
'''def multiply(a,b):
    result=a*b
    print(result)
multiply(5,2)'''
#Write a Python program to create a function named subtract() that takes two numbers as arguments and prints their difference.
'''def multiply(a,b):
    result=a-b
    print(result)
multiply(4,3)'''

#Write a Python program to create a function named divide() that takes two numbers as arguments and prints their division.
'''def divide(a,b):
    result=a/b
    print(result)
divide(10,5)'''
#Write a Python program to create a function named greet() that takes a person's name as an argument and prints:
'''def greet(name):
    
    print("hello",name)
greet("mudeer")'''
#Write a Python program to create a function named cube() that takes a number as an argument and prints its cube.
'''def cube(a):
    result=a*a*a
    print(result)
cube(5)'''
#Write a Python program to create a function named is_even() that takes a number as an argument and prints Even if the number is even, otherwise prints Odd
'''def iseven(a):
    if a%2==0:
        print("even")
    else:
        print("odd")
iseven(5)'''
#Write a Python program to create a function named largest() that takes two numbers as arguments and prints the larger number.
'''def largest(a,b):
    if a>b:
        print("a is largest",a)
    elif a==b:
        print("a is equal to b")
    else:
        print("b is largest",b)
largest(5,5)'''
#Write a Python program to create a function named max_of_three() that takes three numbers as arguments and prints the largest number.
'''def max_of_three(a,b,c):
    if a > b and a > c:
        print(a)
    elif a==b and a==c:
        print("a=b=c")
    elif b>a and b>c:
         print(b)
    else:
        print(c)
max_of_three(2,3,4)'''
#Write a Python program to create a function named square() that takes a number as an argument and returns its square.
'''def square(a):
    result = a*a
    return result
c=square(5)
print(c)'''
#Write a Python program to create a function named add() that takes three numbers as arguments and returns their sum.
'''def add(a,b,c):
    result=a+b+c
    return result
c=add(2,3,4)
print(c)'''
#Write a Python program to create a function named multiply() that takes two numbers as arguments and returns their product.
'''def multiply(a,b):
    result=a*b
    return result
c=multiply(2,3)
print(c)
'''
#Write a Python program to create a function named check_even() that takes a number as an argument and returns "Even" if the number is even, otherwise returns "Odd".
'''def check_even(a):
    if a%2==0:
        return "a is even"
    else:
        return "a is odd"
c=check_even(3)
print(c)'''
#Write a Python program to create a function named absolute_value that takes a number as an argument and returns its positive value
'''def absolute_value(a):
    if a<=0:
        return a*-1
    else:
        return a
c=absolute_value(-4)
print(c)'''
#Write a Python program to create a function named largest() that takes two numbers as arguments and returns the larger number.
'''def largest(a,b):
    if a>b:
        return a
    else:
        return b
c=largest(2,3)
print(c)'''
#Write a Python program to create a function named smallest() that takes two numbers as arguments and returns the smaller number.
'''def smallest(a,b):
    if a > b:
        return b
    else:
        return a
result=smallest(2,3)
print(result)'''
#Write a Python program to create a function named is_positive() that takes a number as an argument and returns True if the number is positive, otherwise returns False.
'''def is_positive(a):
    if a >0 :
        return True
     
    else:
        return False
result=is_positive(3)
print(result)'''
#Write a Python program to create a function named is_even() that takes a number as an argument and returns True if the number is even, otherwise returns False.
'''def is_even(a):
    if a %2==0 :
        return True
     
    else:
        return False
result=is_even(3)
print(result)'''
#Write a Python program to create a function named is_greater() that takes two numbers as arguments and returns True if the first number is greater than the second number, otherwise returns False.
'''def is_greater(a,b):
    if a > b:
        return True
     
    else:
        return False
result=is_greater(3,6)
print(result)'''
#Write a Python program to create a function named 
#is_divisible() that takes two numbers as arguments and returns True
#if the first number is divisible by the second number, otherwise returns False(directly)
'''def is_divisible(a,b):
    return a%b==0
result=is_divisible(3,2)
print(result)'''
#Write a Python program to create a function named calculate_area() that takes the length and width of a rectangle as arguments and returns its area.
'''def calculate_area(a,b):
    area=a*b
    return area
result=calculate_area(2,3)
print("the area of rectangle is ",result)'''
#Write a Python program to create a function named calculate_perimeter() that takes the length and width of a rectangle as arguments and returns its perimeter
'''def calculate_perimeter(a,b):
    perimeter=2*(a+b)
    return perimeter
result=calculate_perimeter(2,3)
print("the perimeter of rectangle is",result)'''
    