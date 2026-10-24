#-----------------LAMBDA------MAP-------FILTER--------REDUCE-------------------------------------------------------
#Write a Python program using a lambda function that takes a number as input and returns its cube.
'''a=int(input("enter the number : "))
cube = lambda a : a*a*a
print(cube(a))'''
#Write a Python program using a lambda function that takes two numbers as input and returns the larger number.
'''a=int(input("enter number 1 :"))
b=int(input("enter number 2 :"))
answer= lambda a,b: a if a > b else b
print(answer(a,b))'''
#Write a Python program using a lambda function that takes a number as input and returns "Even" if the number is even, otherwise returns "Odd
'''a=int(input("enter the number : "))
answer= lambda a : "even" if a % 2 == 0 else "odd"
print(answer(a))'''
#Write a Python program that takes five numbers as input and uses map() with a lambda function to calculate the square of each number
'''user=str(input("enter a list of number "))
numbers=list(map(int,user.split()))

answer=list(map(lambda x:x*x,numbers))
print(answer)'''
#rite a Python program that takes a list of numbers as input and uses map() with a lambda function to multiply each number by 3.
'''user=str(input("enter the list of numbers : "))
numbers=list(map(int,user.split()))
answer=list(map(lambda a : a * 3 , numbers))
print(answer)'''
#write a Python program that takes a list of numbers as input and uses map() with a lambda function to add 10 to each number.
'''user=str(input("enter the number :")).split()
numbers=list(map(int,user))
answer=list(map(lambda a : a + 10 , numbers))
print(answer)'''
#Write a Python program that takes a list of numbers as input and uses map() with a lambda function to convert each number into its cube.
'''user=str(input("enter the number : ")).split()
numbers=list(map(int,user))
print(list(map(lambda c : c * c * c, numbers)))'''
#Write a Python program that takes a list of numbers as input and uses map() with a lambda function to convert each number into its absolute value
'''user=str(input("enter the number : ")).split()
numbers=list(map(int,user))
print(list(map(lambda c : abs(c),numbers)))'''
#----------------------------------------FILTER-------------------------------------------------------------
#Write a Python program that takes a list of numbers as input and uses filter() with a lambda function to select only the positive numbers
'''user=str(input("enter a list of numbers : "))
numbers=list(map(int,user.split()))
answer=list(filter(lambda a : a>0 , numbers))
print(answer)'''
#write a Python program that takes a list of numbers as input and uses filter() with a lambda function to select numbers greater than 10.
'''user=str(input("enter the number")).split()
numbers=list(map(int,user))
print(list(filter(lambda a : a > 10 , numbers)))'''
#rite a Python program that takes a list of numbers as input and selects only the negative numbers using filter() and lambda.
'''user=str(input("enter a list of numbers : "))
numbers=list(map(int,user.split()))
answer=list(filter(lambda a : a<0 , numbers))
print(answer)'''
#Write a Python program that takes a list of numbers as input and uses filter() with a lambda function to select numbers divisible by 5.
'''user=str(input("enter the numbers : ")).split()
numbers=list(filter(lambda a : a % 5 == 0 ,map(int,user)))
print(numbers)'''
#Write a Python program that takes a list of numbers as input and uses reduce() with a lambda function to calculate the product of all numbers.
'''from functools import reduce 
user=str(input("enter the number ")).split()
numbers=map(int,user)
answer=reduce(lambda a, b: a * b , numbers)
print(answer)'''
#Write a Python program that takes a list of numbers as input and uses reduce() with a lambda function to find the maximum number.
'''from functools import reduce
user=str(input("enter the number :")).split()
numbers=list(map(int,user))
answer=reduce(lambda a , b : a if a > b else b , numbers)
print(answer)'''
#Write a Python program that takes a list of numbers as input and uses reduce() with a lambda function to calculate the sum of all even numbers.
from functools import reduce
user=str(input("enter the number ")).split()
numbers=list(filter(lambda a : a %2 == 0,map(int,user)))
print(reduce(lambda a , b: a+b  ,numbers))