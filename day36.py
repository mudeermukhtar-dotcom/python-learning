#-----COUNT THE NUMBER OF VOWELS AND CONSONENTS IN A FILE---------------------
'''with open('day36.txt','r') as file:
    x=file.read()
    print(x)
    vowels=["a","e","i","o","u","A","E","I","O","U"]
    countv=0
    countc=0
    for i in x:
        if i in vowels and i.isalpha():
            countv=countv+1
        elif i.isalpha():
            countc = countc +1
    print(f"THE FILE CONSISTS OF {countv} VOWELS")
    print(f"THE FILE CONSISTS OF {countc} CONSONENTS")'''
#__________________________________________________________________________________
#--------------FIND THE LONGEST WORD IN FILE ----------------------------------
'''with open('day36.txt','r') as file:
    x=file.read()
    y=x.split()
    longest=y[0]
    letters=0
    for i in y:
       if len(str(i)) > len(longest):
           longest=i
           letters=len(i)
           
            
    print(f"THE LON=NGEST WORD IN THE FILE IS {longest}")   
    print(f"THE LETTERS PRESENT IN THE LARGEST WORD IS {letters}")  '''
#___________________________________________________________________________________
#--------------------COUNT THE FREQUENCY OF EACH WORD------------------------------
'''with open('day36.txt', 'r') as file:
    x=file.read()
    y=x.split()
    user=input("ENTER WORD")
    count=0
    for i in y:
     if user in i :
        count=count+1
print(f"THE FREQUENCY OF {user} if {count}")'''
