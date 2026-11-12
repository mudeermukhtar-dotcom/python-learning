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
