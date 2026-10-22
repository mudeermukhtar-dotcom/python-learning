#Write a Python program to print all prime numbers from 1 to n ussing for loop:
'''n=int(input("enter the number : "))
numbers=[]
for i in range(2,n+1):
    count=0
    for m in range(1,i+1):
        if i % m == 0:
            count=count+1
    if count == 2:
     numbers.append(i)
print(numbers)'''
#Write a Python program to print all prime numbers from 1 to n ussing while loop:
'''n=int(input("enter the number : "))
number=[]
i=2
while i <= n:
    count=0
    j=1
    while j <= i:
        
        if i % j ==0:
            count=count+1
   
       
        j=j+1 
    if count== 2:
              number.append(i)
    i=i+1
print(number)'''
#Write a Python program to repeatedly add the digits of a number until only one digit remains.
'''user=int(input("enter the number : "))
total=0
n=user
final=0
while total >= 0:
    final =0  
    while total > 0:
     final=final + total%10
     total=total//10
print(final)'''
    
        