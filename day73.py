#revision 
#1) print numbers fro 1 to 20
'''for i in range(1,21):
    print(i)'''
#2) Print all even numbers from 1 to 50.
'''for i in range(2,51,):
    if i % 2 ==0:
     print(i)'''
#3) reverse a number:
'''user=int(input("enter the nunmber "))
rev=0
while user > 0:
    rev=(rev*10)+user%10
    user=user//10
print(rev)'''
#4 )  Sum of digits
'''user=int(input("enter the number "))
sum=0
while user > 0:
    number=user%10
    sum += number
    user=user//10
print(sum)'''
#q5 armstrong number
'''user=str(input("enter the number "))
length=len(str(user))
sum=0
orginal_number=int(user)
for i in user:
    i=int(i)
    sum +=i**length
if sum == orginal_number:
    print("armstrong")
else:
    print("not an armstrong")'''
#q6 prime numbers from 1 to 100:
'''prime_list=[1,]
for i in range(2,101):
    count =0
    for j in range(1,i+1):
        if i % j == 0:
            count +=1
    if count == 2:
        prime_list.append(i)
print(prime_list)'''
#q7 star pattern
cols=int(input("enter the number"))
for i in range(0,cols+1):
    for j in range(cols-i):
        print(" ",end="")
    for k in range(2*i+1):
        print("*",end="")
    print()

        
        
    
    

        
    