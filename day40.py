#Write a Python program that counts how many even digits and odd digits are present in a given number.
'''user=int(input("enter the number"))
even_number=0
odd_number=0
while user > 0:
    if (user%10)% 2 ==0:
        even_number += 1
    else:
        odd_number += 1
    user=user//10
print(f"EVEN NUMBERS : {even_number}")
print(f"ODD NUMBERS : {odd_number}")'''
#Write a Python program that finds the sum of even digits and the sum of odd digits separately
'''user=int(input("enter the number"))
even_sum=0
odd_sum=0
while user >0:
    if  (user%10) % 2 ==0:
        even_sum = even_sum +  user% 10
    else:
        odd_sum = odd_sum + user%10
    user=user//10
print("EVEN SUM :",even_sum)
print("ODD SUM :",odd_sum)'''
#Write a Python program to reverse a number without using str() or slicing.
'''user=int(input("enter the number : "))
rev=0
while user > 0:
    rev=(rev*10)+user%10
    user=user//10
print(f"REVERSE : ",rev)
    '''
#check wheter the number is palindrome or not
'''user=int(input("enter the number : "))
orginal_no=user
rev=0
if user > 0:
 while user > 0:
    rev=(rev*10)+user%10
    user=user//10
 if rev == orginal_no:
    print(f"the number {orginal_no} is palindrome")
 else:
    print(f"the number {orginal_no} is not  palindrome ")
elif user < 0:
     print(f"the number {orginal_no} is not  palindrome ")
else:
    print("the number is palindrome")'''
#check wheter the number is armstrong or not
'''user=int(input("enter the number"))
total=0
orginal_no=user
while  user > 0:
    x=user%10
    cube=x*x*x
    total=total+cube
    user=user//10
if total == orginal_no:
    print("the number is armstrong")
else:
    print("the number is not armstrong")  '''  
#write a Python program to find the factorial of a number using a while loop.    
'''n=int(input("enter the  number"))
total=1
while n > 0:
    digit=n
    total=digit*total
    n=n-1
print(total)'''
#Write a Python program to check whether a number is prime or not using a while loop.
'''n=int(input("enter the number"))
count=0
i=1
if n == 0 or n == 1:
 print("the numbver is not prime")
elif n < 0:
    print("the number is not prime")
else:
 while  i <= n:
   if n % i == 0:
       count += 1
   i=i+1 
 if count > 2 :
    print("the number is not a prime number")
 elif count == 2:
    print("the numberr is prime") 
 else:
     print("the number is not prime")'''
