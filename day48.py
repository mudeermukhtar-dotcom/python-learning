#password checker
'''while True:
 user=input("enter the password ")
 if len(user)>= 8:
    countd=0
    countu=0
    countl=0
    for i in user:
        if i.isdigit():
            countd += 1
        if i.islower():
            countl += 1
        if i.isupper():
            countu +=1
    if countl >= 1 and  countu >= 1 and countd >=1:
        print("password is strong")
        break
    else:
        print("password must contain a digit ,a lower case , a upper case")
 else:
    print("length of password should be greater than 7") ''' 
#
'''while True:
    user=str(input("enter the password"))
    if len(user) >= 8:
        countd=0
        countu=0
        countl=0
        counts=0
        for i in user:
            if i.isdigit():
                countd += 1
            if i.isupper():
                countu += 1
            if i.islower():
                countl += 1
            if not i.isalnum():
                counts += 1
        if countd >= 1:
            if countu >= 1:
                if countl >= 1:
                    if counts >= 1:
                        print("password is strong")
                        break
                    else:
                        print("add atleast one special chacater to your password")
                else:
                    print("add lower case to your password")
    
            else:
                print("add upper case to your password")
        else:
            print("add digits to password")
    else:
        print("the password should be greater than 7 letters")'''
                                        
#
'''while True:
    user=str(input("enter the password"))
    if len(user) >= 8:
        countd=0
        countu=0
        countl=0
        counts=0
        for i in user:
            if i.isdigit():
                countd += 1
            if i.isupper():
                countu += 1
            if i.islower():
                countl += 1
            if not i.isalnum():
                counts += 1
        if countd >= 1 and countl >= 1 and countu >= 1 and counts >= 1:
            print("password is strong")
            break
        if countd <1:
            print("add one more digit ")
        if countl < 1:
            print("add one lower case ")
        if countu < 1:
            print("add one upper case")
        if counts < 1:
            print("add one special character")
    else:
        print("lenngth of password should be >= 8")
                        '''
                