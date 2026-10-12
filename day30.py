# Square-partern
"""rows=int(input("enter the number of starts for a row and columb"))
for i in range(0,rows):
    for j in range(0,rows):
     print("*" ,end=" " )
    print()"""

# Right-Angled-traingle
"""col=int(input("enter the columbs"))
for  i in range(0,col+1):
    j=i
    for j in range(0,i):
        print("*",end=" ")   
    print()"""
# Inverted-traingle
"""col=int(input("enter columbs")) 
for i in range(col,-1,-1): 
    for j in range(i): 
        print("*",end =" ")
    print()"""
# number right angle traingle
'''col=int(input("enter cols : "))
for i in range(1,col+1):
    for k in range(1,i+1):
        print(k ,end="")
    print( )'''
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
#nverted Pyramid
'''cols=int(input("enter the cols : "))
for i in range(cols,0,-1):
    for j in range(cols-i):
        print(" ",end="") 
    for k in range(2*i-1):
        print("*",end="")
    print()'''
#diamond shape 
'''cols=int(input("enter the cols"))
total_columb=cols+cols-1
for i in range(1,cols+1):
    for j in range(cols-i):
        print(" ", end="")
    for k in range(2*i-1):
        print("*" , end="")
    print()
for l in range(cols-1,0,-1):
    for m in range(cols-l):
        print(" ", end="")
    for n in range(2*l-1):
        print("*", end="")
    print()'''
#Hollow Square Star Pattern
'''cols=int(input("enter cols : "))

space=cols-2
for i in range(0,cols+1):
    if i == 0:
        for s in range(0,cols):
            print("*" , end="")
        print()
    elif i > 0 and i < cols:
       
        for z in range(1):
          print("*", end="")
        for k in range(space):
          print(" " , end = "")
        for l in range(1):
          print("*" , end="")
        print()
    else:  
      for x in range(0,cols):
        print("*" , end="")
      print()'''
#hollow square pattern(short):
cols = int(input("Enter columns: "))

for i in range(0,cols+1):
    for j in range(0,cols+1):
        if i == 0 or i == cols:
            print("*", end="")
        elif j == 0 or j == cols:
            print("*", end="")
        else:
            print(" ", end="")
    print()