#Write a Python program that takes an integer and counts how many even digits and how many odd digits are present in it.
'''i=int(input("enter the numbe"))
counte=0
counto=0

    
while i > 0:
    num=i%10
  
    if num %2==0:
        counte=counte+1
    if num % 2 !=0:
        counto=counto+1
    i=i//10
print("even numbers:",counte,)
print("odd numbers:",counto)'''

#Write a Python program that takes an integer n and prints the sum of all even numbers from 1 to n.

'''n=int(input("enter the number"))
sum=0
i=2
while i <= n:
    sum=sum+i
    i=i+2
print(sum)'''
#Write a Python program to create a tuple containing 5 numbers and print the third element of the tuple.
'''tuple1=(1,2,3,4,5)
print(tuple1[2])'''
#Write a Python program to create a tuple of 5 numbers and print the last element using negative indexing.
'''tuple1=(1,2,3,4,5)
print(tuple1[-1])'''
#Write a Python program to create a tuple of 6 numbers and print all the elements from the 2nd element to the 5th element using slicing.
'''tuple1=(1,2,3,4,5,6)
print(tuple1[1:-1])'''
#Write a Python program to create a tuple of 5 numbers and check whether the number 3 is present in the tuple or not.
'''tuple1=(1,2,3,4,5,6)
if 3 in tuple1:
    print("yes")
else:
    print("no")'''
#Write a Python program to count how many times the number 2 appears in a tuple
'''tuple1=(1,2,3,4,5,2,4,5,2)
print(tuple1.count(2))'''
#Write a Python program to find the position (index) of the number 4 in a tuple
'''tuple1=(1,2,3,4,5,2,4,5,2,6)
print(tuple1.index(6))'''
#Write a Python program to find the length of a tuple containing 10 elements
'''tuple1=(1,2,3,4,5,2,4,5,2,6)
print(len(tuple1))'''
#Write a Python program to print every element of the following tuple using a for loop:
'''tuple1=(1,2,3,4,5,2,4,5,2,6)
for i in tuple1:
    print(i)'''
#e a Python program to print only the even numbers from the tuple using a for loop.
'''tuple1=(1,2,3,4,5,2,4,5,2,6)
for i in tuple1:
    if i %2==0:
        print(i)'''
#Write a Python program to find the sum of all elements in the tuple using a for loop.
'''numbers = (10, 20, 30, 40, 50)
sum=0
for i in numbers:
    sum=sum+i
print(sum)'''
#Write a Python program to count how many even numbers are present in the tuple using a for loop.
'''numbers = (12, 7, 4, 19, 8, 3)
count=0
for i in numbers:
    if i % 2==0:
        count = count +1
print(count)'''
#Write a Python program to find the largest number in the tuple using a for loop.
'''numbers = (12, 7, 4, 19, 8, 3)
largest=numbers[0]
for i in numbers:
    if i > largest:
        largest=i
print(largest)'''
#Write a Python program to unpack the tuple into three variables a, b, and c, and then print all three variables.
'''numbers = (10, 20, 30)
a,b,c=numbers
print(a)
print(b)
print(c)'''
#Write a Python program to unpack these values into name, age, and course, then print them.
'''student = ("Mudeer", 18, "CSE")
name,age,stream=student
print(name)
print(age)
print(stream)'''
#Unpack the tuple into four variables a, b, c, d and print their sum:
'''numbers = (5, 10, 15, 20)
a,b,c,d=numbers
sum=a+b+c+d
print(sum)'''
#Unpack the tuple into name, age, course, and semester, then print only course and semester.
'''student = ("Mudeer", 18, "CSE", 1)
name,age,course,semister=student
print(course,semister)'''
#Write a Python program to combine both tuples into one tuple using +, then print the result.
'''t1 = (1, 2, 3)
t2 = (4, 5, 6)
t3=t1+t2
print(t3)'''
#Write a Python program to combine both tuples into a new tuple called skills and print the result.
'''t1 = ("Python", "HTML")
t2 = ("CSS", "JavaScript")
skills=t1+t2
print(skills)'''
#Write a Python program to combine all three tuples into one new tuple called numbers and print the result.
'''t1 = (10, 20)
t2 = (30, 40)
t3 = (50, 60)
numbers=t1+t2+t3
print(numbers)'''
#Write a Python program to repeat this tuple 3 times using the * operator and print the result.
'''numbers=(1,2,3)
new=numbers*3
print(new)'''
#write a Python program to repeat this tuple 2 times using the * operator and print the result.
'''words = ("Python", "CSE")
new=words*2
print(new)'''
#Write a Python program to convert the list into a tuple using tuple() and print the result
'''numbers = [10, 20, 30, 40, 50]
numbers=tuple(numbers)
print(numbers)'''
#Write a Python program to convert the tuple into a list using list() and print the result.
'''numbers = (10, 20, 30, 40, 50)
numbers = list(numbers)
print(numbers)'''