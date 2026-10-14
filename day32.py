# traaingle
"""cols=5
for i in range(1,cols+1):
    for j in range(i):
        print("*",end="")

    for k in range(cols-i):
        print(" ", end="")
    print()
for l in range(cols-1,0,-1):
    for m in range(l):
        print("*",end="")
    for n in range(cols-l):
        print(" ", end="")
    print()"""

# butter fly
"""cols=int(input("enter the cols"))
for i in range(1,cols+1):
    for j in range(i):
        print("*",end="")
    for k in range(2*(cols-i)):
        print(" ", end="")
    
    for m in range(i):
        print("*",end="")
        
    print()
for a in range(cols-1,0,-1):
    for b in range(a):
        print("*", end="")
    for c in range(2*(cols-a)):
        print(" ", end="")
    for d in range(a):
        print("*", end="")
    print()"""
# floyd's traingle:
"""n=int(input("enter the number"))
sum=0
for i in range(0,n):
    for j in range(i+1):
        sum=sum+1
        print(sum, end=" ")
    print()"""
# inverted-floyds-traingle:
"""n=int(input("enter the number"))
total=0
for i in range(0,n):
    for j in range(n-i):
        total=total+1
        print(total,end=" ")
    print()"""
# number pyraqmid:
'''n = int(input("enter the number"))
for i in range(1, n + 1):
    for k in range(n - i):
        print(" ", end="")
    for j in range(1, i + 1):
        print(j, end="")
    for l in range(2,i+1):
        print(i-l+1, end="")

    print()'''
#pnumber similar traingle :
'''n=int(input("enter the numeber"))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ", end="")
    for k in range(i):
        print(i , end=" ")
    print()
    '''
