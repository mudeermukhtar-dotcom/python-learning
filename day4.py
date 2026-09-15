#Write a Python program that takes an integer n as input and prints numbers from 1 to n. Stop the loop completely when the number 7 is reached.
'''n=int(input("enter number ...!"))
i=1
while i <=n:
     print(i)
     if i ==7:
       break
     i=i+1'''
#Write a Python program that takes an integer n as input and prints numbers from 1 to n. Skip the number 5 using the continue statement.
'''n=int(input("enter number...!"))
i=1
while i  <= n:
    if i == 5:
       i=i+1
       continue
    print(i)
    i=i+1'''
#to count even numbers in a given number:

'''i=int(input("enter numberber"))
sum=0

while i>0:
    no=i%10
    if no%2==0:
       sum=sum+1
    i=i//10  
print(sum)'''
#To count odd numbers in a given number

'''i=int(input("enter numberber"))
sum=0

while i>0:
    no=i%10
    if no%2!=0:
       sum=sum+1
    i=i//10  
print(sum)'''
#to make a pattern of nukber 123|246|468 by using nested loop
'''i=1
while i <= 3:
    j = 1
    while j <= 3:
        print(i*j)
        j=j+1

    i=i+1'''
#“Write a Python program using nested while loops to print the following pattern:”
'''i=1
while i <= 3:
    j=1
    while j <= i:
        print("*", end="")
        j=j+1
    i=i+1
    print()'''
#keep asking until marksare in the calid range
'''marks=int(input("marks"))
while marks < 0 or marks>100:
    print("invalid")
    marks=int(input("enter gain"))
print("accepted",marks)'''
#Write a Python program using nested while loops to print the following reverse star pattern:
'''i=5
while i >= 1:
    j=1
    while j<=i:
      print("*" ,end="")
      j=j+1
    i=i-1
    print()'''
#write a python program to follow the patern 1|12|123:
'''i=1
while i <= 3:
    j=1
    while j <=i:
        print(j,end="")
        j=j+1
    i=i+1
    print()'''
#Write a Python program using nested while loops to print this pattern:1|22|333|4444|55554
'''i=1
while i <= 5:
    j=1
    while j<=i:
        print(i,end="")
        j=j+1
    i=i+1
    print()'''
#write a program to print this pattern :1|12|123|1234:
'''i=1
while i <= 5:
    j=1
    while j <= i:
        print(j, end="")
        j=j+1
    i=i+1
    print()'''
#write a program to print this pattern 12345|1234|123|12|1
'''i=5
while i >= 1:
    j=1
    while j <= i:
        print(j,end="")
        j=j+1
    i=i-1
    print()'''
#write a program to print this pattern 54321|5432|543|54|5
'''i=1
while i <= 5:
    j=5-i+1
    while j>=1:
        print(j,end="")
        j=j-1
    i=i+1
    print()'''
    

    
   




  
