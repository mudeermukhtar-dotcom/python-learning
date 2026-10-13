# hollow right angled traingle:
'''cols=int(input("enter the cols"))
for i in range(1,cols+1):
    for j in range(i):
        if   i == cols:
            print("*" , end="" ) 
        elif j == 0 or  j==i-1:
            print("*", end="")
        else:
            print(" ", end="")
    
    print()'''
    
#inverted hollow right angked traingle
'''cols=int(input("enter the cols "))
for i in range(cols,0,-1):
    for j in range(1,i+1):
        if i == cols :
            print("*", end="")
        elif j == 1 or j == i:
            print("*", end="")
        else:
            print(" ", end="")
    print()'''
#hollow pyramid:
'''cols=int(input("enter the number of columbs"))
for i in range(1,cols+1):
    for k in range(0,cols-i):
        print(" ", end="")
    for j in range(2*i-1):
        if i == cols:
         print("*",end="")
        elif j == 0 or j == 2*i-2:
            print("*", end="")
        else:
            print(" ", end="")
   
    print()  ''' 
#inverted hollow pyramid:
'''cols = int(input("enter the number : "))
for i in range(cols,0,-1):
    for k in range(cols-i):
        print(" ", end ="")
        
    for j in range(2*i-1):
        if i == cols:
         print("*", end="")
        elif j == 0 or j == 2*i-2:
            print("*", end="")
        else:
            print(" ", end="")
    print()
     '''
#hollow diamond:
'''cols=int(input("enter the cols : "))
for a in range(1,cols+1):
    for b in range(cols-a):
        print(" " , end="")
    for c in range(2*a-1):
     if  a == 1:
        print("*", end="")
     elif c == 0 or c == 2*a-2:
         print("*", end="")
     else:
         print(" ", end="")
    print()
for d in range(cols-1,0,-1):
    for e in range(cols-d):
        print(" ",end="")
    for f in range(2*d-1):
    
     if f == 0 or f== 2*d-2:
         print("*", end="")
     else:
         print(" ", end="")
    print()'''
  
    
        

    
  
    
        

    
