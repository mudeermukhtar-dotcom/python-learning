#-----------------------------------FILE HANDLING-----------------------------------------------
#q1) WRITE A FILE
'''with open('mudeer.txt','w') as f:
    f.write("hi ! MUDEER")'''
#---------------OR---------------------
'''f=open('mudeer.txt','w')
f.write("HI ! ARE YOU FINE")
f.close()'''#IN THIS METHOD WE HAVE TO CLOSE:
#q2) READ A FILE 
'''f=open('mudeer.txt') #read is defualt in python thatswhy i didnt write 'r' here
print(f.read())
f.close()'''
#q3)APPEND TO A FILE 
'''f=open('mudeer.txt','a')
f.write("HI MUDEER")
f.close()'''
#q4)COUNT A CHARCTER IN A FILE
'''f=open('mudeer.txt','r')
x=f.read()
print(len(str(x)))
f.close()'''
#q5)count lines
'''f=open('mudeer.txt','r')
x=f.readlines()
print(len(x))
f.close()
'''
#q6)
'''f=open('mudeer.txt','r')
x=f.read()
user=str(input("enter :"))
if user in x :
    print(f"{user} found")
else:
    print(f"{user} not found")
f.close()'''
#q7)
'''f=open('mudeer.txt','r')
x=f.read()
user=str(input("enter :"))
count=0
y=x.count(user)
print(f"{user} appears { y } times")'''
#q8)
'''f=open('mudeer.txt','a')
user=input("enter text ")
f.write(user)
f.close()'''
#q9)
'''f=open('mudeer.txt', 'r' )
x=f.read()
y=x.split()
print(len(y))
f.close()'''
#q10
with open('mudeer.txt','r') as f:
    x=f.read()
    print(x)
