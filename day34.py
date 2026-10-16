"----------------------------PRACTICE---QUESTIONS---------------------------------------------"
#q1'''
'''n=5
for i in range(1,6):
    
        
        for j in range(n-i):
            print(" " , end= "")
        for z in range(i):
            print("*", end="")
           
        print()'''
#q2
'''sum=0
for i in range(1,6):
    for j in range(i):
        sum=sum+1
        print(sum ,end=" ")
    print()
    '''
#q3
n=5
for i in range(1,6):
    for j in range(n-i):
     print(" ", end="")
    for k in range(2*i-1)   :
        print("*", end="")
    print()
#q4
'''n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == 1 or i == 5:
            print("*", end=" ")
        elif j == 1 or j == 5:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()'''
#q5
'''n=int(input("enter the number"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if j == i or j == n-i+1:
          print("*",end="")
        else:
            print(" ", end="")
    print()
#q6'''
'''for i in range(1,6):
    for j in range(i):
        print(chr(j+65), end="")
    print()'''
