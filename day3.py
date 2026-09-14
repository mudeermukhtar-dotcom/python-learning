#count numbers divisible by 5 and 3
'''n=int(input("enter number here...!"))
i=1
count=0
while i<=n:
    if i%3==0 and i%5==0:
        count=count+1
    i=i+1
print(count)'''
#find the factorial of a number
'''n=int(input("enter number here"))
i=n
sum=1
while i >= 1:
    sum=sum*i
    i=i-1
print(sum)'''
#swapping of 2 of a nunber
'''n1=int(input("enter number 1"))
n2=int(input("enter number 2"))
temp=n1
n1=n2
n2=temp
print(n1,n2)'''
#reverse of a number
'''i=int(input("enter number here"))
rev=0
while i >= 1:
    rev=(rev*10)+i%10
    i=i//10
print(rev)'''
#count the number of digits in a number
'''i=int(input("enter number"))
count=0
while i >= 1:
    count=count+1
    i=i//10
print(count)'''
#find the sum of digits ofa number
'''i=int(input("enter the number"))
sum=0
while i >= 1:
    sum=sum+(i%10)
    i=i//10
print(sum)'''
#to check whether a number is palindrone or not
'''i = int(input("enter number here"))
original=i
rev = 0
while i >= 1:
 rev = (rev * 10) + i % 10
 i = i // 10

print(rev)
if rev==original:
     print("the number is palindrome")
else:
   print("the number is not palindorme")'''
#to check the largest digit in a given number
'''i=int(input("enter the number"))
largest=0
while i >= 1:
    digit=i%10
    i=i//10
    if digit > largest:
      largest=digit
      print(largest)'''
#to check  the smallest digit in the number 
'''i=int(input("enter the number"))
smallest=i
while i >= 1:
    digit=i%10
    i=i//10
    if digit < smallest:
      smallest=digit
print(smallest)'''
#take password from user until it is correct password
'''password=123
i=int(input("enter number"))
while i!=password:
  i=int(input("enter number"))
  if i==password:
    print(i,"is your passwordf tu mahaan he")'''
#do sum until zero comes in a number
'''i=int(input("enter number"))
while i!=0:
  sum=sum+i
  i=int(input("enter number"))
print(sum)'''
#CHECK GREATEST OF TWO NUMBERS
'''a=int(input("enter number a"))
b=int(input("enter number 2"))
if a>b:
    print(a,"is greater thaan",b)
else:
    print(b,"is greater than ",a)'''
  
    

