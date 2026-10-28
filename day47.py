#personal introduction generator:
#--------------------------personal induction-----------------------------------------------------
'''name=input(" enter your name : ").title()   #takes name from user
age=int(input("enter your age : "))    #takes age from user
city=input("enter your city :") .title()   #takes city from user
print(f"i am {name}.\ni am {age} years old.\ni live in {city}") #prints introduction'''
#word analyser
'''user=input("enter the word : ")   #takes inout from user
print(user.upper())    #prints the word in upper case
print(user.lower())    #prints thw word in lower case
print(len(user))       #prints the length of word
print(user[0])         #prints the first letter of word
print(user[-1])        #prits the last letter of word
print(user[::-1])      #prints the word in reverse'''
#word generator
'''user=input("enter your full name : ") #te=akes word from user
print(user.strip())    #remove extra spaces 
print(user.lower())    #comvert  all to lower csase
print(user[0:3])       #prints first three characters
print(user[-3:])     #last 3 characters
print(user[::-1])   #reversed word'''
#sentence cleaner
'''user=input("enter the sentence : ").strip()    
print("CLEANED SENTENCE : " ,user.lower())
print("LENGTH OF USER : " ,len(user))
print("THE FIRST CHARACTER : ",user[0])
print("THE LAST CHARACTER : ",user[-1])
print("THE REVERSED SENTENCE : ",user[::-1])
'''
#username generator
'''user=str(input("enter the name : ")).strip().title()
birthyear=int(input("enter the birth year"))
city=input("enter your city : ")
print("LENGTH OF NAME :\t",len(user))
print("REVERSED NAME :\t",user[::-1])
by=str(birthyear)
print(city.upper())
print(city.lower())
print(user[0:3]+user[-3:]+by[-2:])'''
#
'''name=input("enter your name : ")
clean_name=name.strip().title()
age=str(input("enter your DOB : "))
sentence=str(input("enter sentence : "))
print("THE LENGTH OF ORGINAL NAME IS ", len(name))
print("THE LENGTH OF CLEAN NAME IS ", len(clean_name))
words=name.split()
print("THE FIRST NAME IS : ",words[0])
print("THE LAST NAME IS : ",words[-1])
print("THE REVERSED NAME IS : ",name[::-1])
print("THE LAST 5 LETTERS OF SENTENCE IS :",sentence[-5:])'''








