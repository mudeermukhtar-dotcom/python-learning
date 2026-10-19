#---------------------------LAMBDA FUNCTIONS------------------------------
#write a Python program that uses a lambda function to find the square of a number:
'''n=int(input("enter a number"))
square=lambda n : n * n
print(square(n))'''
#Write a Python program using a lambda function to calculate the cube of a number.
'''n=int(input("emter the number"))
cube=lambda n:n*n*n 
print(cube(n))
'''
#Write a Python program using a lambda function to add two numbers entered by the user.
'''a=int(input("enter the number"))
b=int(input("enter the number"))
sum=lambda  a,b:a+b
print(sum(a,b))'''
#Write a Python program using a lambda function to find the greater of two numbers.
'''a=int(input("enter num 1"))
b=int(input("enter num 2"))
greater=lambda a,b: a if a > b else b
print(greater(a,b))'''
#Write a Python program using a lambda function to check whether a number is even or odd.
'''a=int(input("enter num "))
check=lambda a : "even" if a % 2 == 0 else "odd"
print(check(a))'''
#write a Python program using a lambda function to convert a temperature from Celsius to Fahrenheit.
'''num=int(input("enter the temperatue in celcius"))
farenhiet=lambda num:(num*9/5)+32
print(farenhiet(num))'''
#count the letters in a string
'''word=input("enter the  word")
length=lambda word:len(word)
print(length(word))'''
#Write a Python program that takes a list of numbers and prints the second-largest number without using sort:
'''user=str(input("enter the numbers"))
list=user.split()
largest=float('-inf')
second_largest=float('-inf')
for i in list:
   if int(i) > largest:
       second_largest=largest
       largest=int(i)
   elif  int(i) < largest and int(i) > second_largest:
       second_largest=int(i)
print(second_largest)'''



    