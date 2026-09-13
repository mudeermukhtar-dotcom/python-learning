#User se n input lo aur 1 se n tak numbers print karo.
'''n=int(int(input("enter number")))
i=1
while i <= n:
 print(i)
 i=i+1'''
#User se n input lo aur 1 se n tak sirf even numbers print karo using a while loop.
'''n=int(input("enter number"))
i=2
while i <= n:
    print(i)
    i=i+2'''
#User se n input lo aur 1 se n tak numbers ka sum nikalo using while loop.
'''n=int(input("enter the number"))
i=1
sum=0
while i<=n:
    sum=sum+i
    i=i+1
print(sum)'''
#User se n input lo aur n se 1 tak numbers print karo using while loop.
'''n=int(input("enter number here"))
i=n
while i >= 1:
    print(i)
    i=i-1'''
#User se n input lo aur 1 se n tak kitne even numbers hain, ye count kar.
'''n=int(input("enter number"))
count=0
i=0
while i <= n:
  i=i+1
  if i%2==0:
    count=count+1
print(count)'''
#user se input n lelo aur n tk even number ka sum kro 
'''n=int(input("enter number"))
i=0
sum=0
while i <= n:
  if i%2==0:
   sum=sum+i
  i=i+1
print(sum)'''
#user se inpout lelo aur n tk saare odd ka sum
'''n=int(input("enter the number"))
i=1
sum=0
while i <= n:
    sum=sum+i
    i=i+2
print(sum) '''
#user se inpout lelo aur n tk saare odd ka sum
'''n=int(input("enter the number"))
i=1
sum=0
while i <= n:
    if i%3 ==0:
     sum=sum+i
    i=i+1
print(sum)   '''
#user se aik number lelo usme saare even ka sum aur odd ka sum nikalo
n=int(input("enter number here"))
i=1
sum=0
sum1=0
while i <= n:
    if i%2 ==0:
        sum=sum+i
    else:
        sum1=sum1+i
    i=i+1
    print(sum,sum1)