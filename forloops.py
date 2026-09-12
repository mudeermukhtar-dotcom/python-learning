#1)user se number n lena aur 1 to n print krna
'''n=int(input("enter number"))
for i in range(1,n,1):
    print(i)'''
#2)user see number ;lena aur  n to 1 prinmt krna
'''n=int(input("enter number n"))
for i in range(n,1,-1):
    print(i)'''
#3)user se imput n lelo aur sum kro 1 to n
'''n=int(input("enter number n"))
sum=0
for i in range(1,n+1):
    sum=sum+i
print(sum)'''
#4)user se number n lelo aur us n tk saare even number likho
'''n=int(input("enter number n"))
for i in range(0,n+1,2):
     print(i)'''
#5)user se input  lelo aur n tk saare odd number likho
'''n=int(input("enter number n"))
for i in range(1,n+1,2):
 print(i)
'''
#6)user se number n lelo aur us number ka table likho 10 tk
'''n=int(input("enter number n"))
for i in range(1,11):
    product=n*i
    print(n,"*",i,"=",product)'''
#7)user se number lelo n aur 1 to n saare odd number ane chahoye
'''n=int(input("enter the number"))
for i in range(1,n):
    if i%3==0:
     print(i)'''
#8)user se number lelo n phirn tk saare even no ka sum nikalo
'''n=int(input("enter the number"))
sum=0
for i in range (0,n):
  if i%2==0:
    sum=sum+i
print(sum)'''
#user se number n leloaur 5 ke multiplles fko print mt kro
'''n=int(int(input("enter number")))
for i in range(1,n+1):
    if i%5==0:
     continue
    else:
     print(i)'''
#User se n input lo aur 1 se n tak numbers print karo.Lekin jaise hi 5 aaye, loop ko completely stop kar do.
n=int(input("enter number"))
for i in range(1,n+1):
    if i==5:
     break
    else:
       print(i)

   




