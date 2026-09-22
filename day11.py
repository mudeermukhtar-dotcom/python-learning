#q19
'''a=1000
b=200
c=60
if a > b and a > c :
    print(a,"is largest")
elif b > c:
     print(b,"is largest")
else:
     print(c,"is largest")'''
#q20''
'''a=10
b=2
c=6
if a < b and a < c :
    print(a,"is smallest")
elif b < a and b < c:
     print(b,"is smallest")
else:
     print(c,"is smallest")'''
#q21
''''marks=int(input("enter the number of marks"))
if marks >= 90:
    print("GRADE A")

    elif marks >=75:
    print("GRADE B")
elif marks >= 60:
    print('GRADE C')
elif marks >= 40:
    print("GRADE C")
else:
    print("GRADE D")'''
#22
'''age=int(input("enter the age"))
if age > 0 and age <= 12:
    print("CHILD")
elif age > 12 and age <= 19:
    print("TEENAGERR")
elif age > 19 and age <= 59:
    print("ADULT")
elif age < 0:
    print("age cant be nagative ..")
else:
    print("SENIOR CITIZEN")'''
#q23:
'''number=int(input("enter the number"))
if number == 1:
    print("MONDAY")
elif number == 2:
    print("TUESDAY")
elif number == 3:
    print("WEDNESDAY")
elif number == 4:
    print("THRUSDAY")
elif number == 5:
    print("FRIDAY")
elif number == 6:
    print("SATURDAY")
elif number == 7:
    print("sunday")
else:
    print("INVALID DAY")'''
#Write a Python program to create a new list containing numbers that are present in numbers1 but not present in numbers2.
'''numbers1 = [4, 7, 2, 9, 5, 10]
numbers2 = [7, 3, 2, 8, 5]
new_list=[]
for i in numbers1:
    if i not in numbers2:
     new_list.append(i)
print(new_list)'''
#print the vowels and consonents in a given word:
'''str=input("enter character")
vowels=["a","e","i","o","u"]
newlistc=[]
newlistv=[]
for k in str:
    if k not in vowels:
        newlistc.append(k)
    else:
        newlistv.append(k)
print("consonents are",newlistc)
print("th vowels are",newlistv)'''
#print wheter the  character is consonent or vowel:
'''ch = input("enter")
if len(ch) == 0:
    print("enter valid")
elif ch.isdigit():
    print("number")
elif ch in "a,e,i,o,u,A,E,I,O,U":
    print("vowel")
elif ch.isalpha():
    print("consonent")
else:
    print("special character") ''' 
#F STRING   
#Write a Python program that takes the user's name and age as input and prints:
'''name=str(input("enter your name"))
age=int(input("enter your age"))
print(f"my name is {name} and i am {age} years old!")'''
#write a Python program that takes two numbers from the user and uses an f-string to print their sum:
'''num1=int(input("enter number 1"))
num2=int(input("enter num 2"))
sum=num1+num2
print(f"sum of  {num1} and {num2} is {sum}")'''
#Write a Python program that takes a number from the user and prints its square and cube using an f-string.
'''a=int(input("enter the number"))
square=a*a
cube=a*a*a
print(f"the square of {a} is {square} and cube is {cube}")'''
#Write a Python program that takes a user's age and prints:
'''age=int(input("enter your  age"))
if age >=  18:
    print(f"you are{age} years old that means you can vote")
else:
    print(f"you are less than {age} that means you cant vote")'''
#Write a Python program that takes 5 numbers from the user, stores them in a list,
# and then prints only the even numbers using an f-string.
'''a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
d=int(input("enter the number"))
e=int(input("enter the number"))
numbers=[a,b,c,d,e]
new_list=[]

for i in numbers:
    if  i %  2== 0:
        new_list.append(i)
print(f"Even numbes are : {new_list}")'''
#Write a Python program that takes 5 numbers from the user, stores them in a list, and finds:
#The largest number
#Its position (index) in the list
'''numbers=[100,12, 45, 7, 89, 34,101]
a=numbers[0]
position=0
for i in numbers:
    if i > a :
     a=i
for i in numbers:
   if i == a:
    print(position)
    break
   position=position+1

print(f"the highest number is  {a} ")'''

#recursiion
#Write a Python function using recursion to print numbers from 1 to n.
'''def increasing(n):
    if n==6:
        return
    print(n)
    increasing(n+1)
increasing(1)'''
#Write a Python function using recursion to print numbers from n down to 1
'''def reverse(n):
    if n == 0:
        return
    print(n)
    reverse(n-1)

reverse(5)'''
#Write a Python function using recursion to print even numbers from 2 to n.
'''def increase(n):
    if n > 10:
        return
    print(n)
    increase(n+2)
increase(2)'''
#Write a Python function using recursion to find the sum of numbers from 1 to n.
'''def sum(n):
    if n ==0 :
     return 0
    
    return n + sum(n-1)

print(sum(5))'''


        
