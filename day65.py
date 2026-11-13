#inverted right angled traingle with number
'''cols=int(input("enter the number : "))
for i in range(cols,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()'''
## Right-Aligned Increasing Star Pattern
'''cols=int(input("enter the cols : "))
for i in range(1,cols+1):
    for j in range(cols-i):
        print(" " ,end="")
    for k in range(i):
         print("*" ,  end="")
    print()'''
## Right-Aligned Decreasing Star Pattern
'''cols=int(input("enter the number of cols : "))
for i in range(cols,0,-1):
    for j in range(cols-i):
        print(" " ,end="")
    for k in range(i):
        print("*" , end="")
    print()
    '''
#Right-Aligned Increasing Number Pattern
'''cols=int(input("enter cols : "))
for i in range (1,cols+1):
    for j in range(cols-i):
        print(" ",end="")
    for k in range(1,i+1):
        print(k,end="")
    print()'''
#: Right-Aligned Decreasing Number Pattern
'''cols=int(input("enter the number : "))
for i in range(cols,0,-1):
    for j in range(cols-i):
        print(" ",end="")
    for k in range(1,i+1):
        print(k,end="")
    print()'''
#Pyramid Star Pattern ⭐
'''cols=int(input("enter the number : "))
for i in range(1,cols+1):
    for j in range(cols-i):
        print(" ", end="")
    for k in range(2*i-1):
        print("*", end="")
    print()'''