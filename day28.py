# short hand if else example 1
"""number=int(input("enter the number"))
result = "even " if number % 2 == 0 else "odd"
print(result)"""

# short hand if else example2
"""a=int(input("enter a"))
b=int(input("enter b"))
result=a if a > b else b 
print(result)"""
# short hand if else example3
"""a=int(input("enter a"))
b=int(input("enter b"))
c=int(input("enter c"))
result=  a if a > b and a > c  else b if b > c else c
print(result) """
# short hand if else example 4
"""a=int(input("enter number"))
result = "positive"if a > 0 else "negative " if a < 0 else 0
print(result)"""
# short hand if else example 5
"""a=int(input("enter marks"))
result="A+" if a > 90 else "A" if a > 75 else "B" if a > 50 else "fail"
print(result)"""
# short hand if else example 6
"""name = input("NAME :")
physics = int(input("enter marks in physics"))
maths = int(input("enter marks in maths"))
coding = int(input("enter marks in programmig"))
chemistry = int(input("enter marks in chemistry"))
average = (physics+maths+coding+chemistry)/4
percentage=((physics+maths+coding+chemistry)/400)*100
grade="A" if percentage > 90 else "B" if percentage > 80 else "C"
print(name)
print(percentage)
print(grade)
print(average)"""
# enumerate functions
# q1)Write a Python program that takes a list of 5 fruits and uses enumerate() to print each fruit along with its index.
"""fruits = ["apple", "banana", "mango", "orange","grapes"]
for index,fruit in enumerate(fruits):
    print(index,")" ,":", fruit)"""
# q2)Write a Python program that takes a list of fruits and uses enumerate() to print only the fruits whose index is even.
"""fruits = ["apple", "banana", "mango", "orange","grapes"]
for index , fruit in enumerate(fruits):
    if index % 2 ==0:
        print(index,")",fruit)"""

# Write a Python program that takes a list of fruits and uses enumerate() to print only those fruits whose index is odd.

'''fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes", "Kiwi"]
for index, fruit in enumerate(fruits):
    if index % 2 != 0:
        print(index, ")", fruit)
'''
#print those frutis only which have length less than 5:
'''fruits=["Apple", "Banana", "Mango", "Orange", "Grapes"]
for index , fruit in enumerate (fruits):
    if len(fruit)<=5:
        print(index,fruit)'''
#print the index of mango
'''fruits=["Apple", "Banana", "Mango", "Orange", "Grapes"]
for index , fruit in enumerate(fruits):
    if fruit == "Mango":
        print(index)'''
        
#start from 1
'''fruits=["Apple", "Banana", "Mango", "Orange", "Grapes"]
for index,fruit in enumerate(fruits , start=1):
    print(index,fruit)'''
#start from 3
'''fruits=["Apple", "Banana", "Mango", "Orange", "Grapes","kiwi"]
for index,fruit in enumerate(fruits ):
    if index >= 3:
     print(index,fruit)'''
#learning import
#Write a Python program that imports the math module and uses it to find the square root of a number.
'''import math
i=float(input(" enter number"))
result = math.sqrt(i)
print(result)'''
#Write a Python program that imports the math module and calculates the factorial of a number using math.factorial()
'''from math import factorial
i=int(input("enter number"))
result=factorial(i)
print(result)'''
#Write a Python program that imports only pi from the math module and calculates the area of a circle.
'''from math import pi
r=float(input("enter radius"))
result = pi * r * r
print(result)'''
#Write a Python program that imports ceil and floor from math and prints both values.
'''from math import ceil , floor
i=float(input("enter number"))
ceiling=ceil(i)
flooring=floor(i)
print(ceiling)
print(flooring)'''
#Write a Python program that imports random and generates a random number between 1 and 10.

'''import random
x=random.randint(1,10)
print(x)'''
#Write a Python program that imports random and randomly chooses one fruit from this list
'''import random
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]
x=random.choice(fruits)
print(x)
'''
     
    
    
