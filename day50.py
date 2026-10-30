#Question: Calculate the Sum of the Factorials of a Number's Digits with str
'''user=input("enter the number").split()
list=list(map(int,user))
sums=[]
sum=0

for i in list:
    i=int(i)
    fact=1
    while i >= 1:
        fact=fact*i
        i=i-1
    sums.append(fact)
for j in sums:
    sum=sum+j
print(f"  the Sum of the Factorials of a Number's Digits is {sum}")'''

'''user=int(input("enter the number"))
or_number=user
#Question: Calculate the Sum of the Factorials of a Number's Digits with int
sums=[]
while or_number > 0:
    number=or_number%10
    or_number=or_number//10
    fact=1
    while number > 0:
        fact=fact*number
        number=number-1
    sums.append(fact)
print(sum(sums))
        '''
#ALL PRIME NUMBER  UPTO N
'''user=int(input("enter the number"))

prime=[]
non_prime=[1]

for j in range(2,user+1):
    i=j 
    count=0  
    while  i > 0:
        if j % i == 0:
            count += 1
            i=i-1
        else:
            i=i-1
   
    if count == 2:
        prime.append(j)
    elif count > 1 :
        non_prime.append(j)
print("PRIME NUMBERS : ",prime)
print("NON PRIME NUMBERS ",non_prime)'''
#revrse a number and chck palindrome
'''user=int(input("enter the number"))
rev=0
orginl_number=user
while user > 0:
    rev=(rev*10)+user%10
    user=user//10
if rev == orginl_number:
    print("it is a plaindrome")
else:
    print("not a palindrome")'''
#check armstrong METHOD 1
'''user=int(input("enter the number"))
length=len(str(user))
total=0
user1=str(user)
for i in user1:
  i=int(i)
  add=i**length
  total=total+add
if user == total:
    print("it is an armstrong nummber")
else:
    print("not an arm strong")  
'''
#ARMSTRONG METHOD 2
user=int(input("enter the number : "))
total=0
length=len(str(user))
orginal=user
while user > 0:
    i=user%10
    user=user//10
    add=i**length
    total=total+add

if total == orginal:
    print("it is an armstrong")
else:
    print("not an armstrong")
    
        
        
        
        
    

    
    
    
    