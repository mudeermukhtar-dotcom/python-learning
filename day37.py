#TELL GIVES US CURRENT POSITION:
'''with open('day37.txt','r') as f:
    f.read(5)
    print(f.tell())'''
#SEEK:
'''with open('day37.txt','r') as f:
    f.seek(6)
    print(f.read(6))'''
#truncate
'''with open('day37.txt','r+') as f:
   f.truncate(3)'''
   
    