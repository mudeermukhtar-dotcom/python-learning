# search number
'''numbers = [12, 25, 37, 48, 59, 64]
search = int(input("enter number that you want to search"))
for i in numbers:
    if search == i:
        print("number found", i)
        break
else:
    print("number not found")'''
#find first even number
'''numbers = [15, 27, 33, 41, 52, 67]
for i in numbers:
    if i % 2 == 0:
      print("FIRST EVEN NUMBER:",i)
      break
else:
    print("no odd number")'''
#find student and number of marks 

'''students = {
    "Aarav": 67,
    "Kabir": 94,
    "Rohan": 81,
    "Dev": 76,
    "Arjun": 89
}
search=str(input("search by name"))
for name ,marks in students.items():
    if search== name :
        print(f"{search} has scoree {marks} marks")
        break
else:
    print("student not found")'''
#Find the first number which is greater than 50:
'''numbers = [12, 27, 31, 45, 53, 68, 72]
for i in numbers :
    if i > 50 :
        print(f"{i} is the first number in list which is greater than 50")
        break
else:
    print("there is no number in list which is greater than 50")'''
#check is there any number in list which is divisible by 7
'''numbers = [11, 23, 37, 41, 55, 67]
for i in numbers:
    if i % 7 == 0:
        print(f"There is a number {i} which is divisble by 7")
        break
else:
    print("there is nno number which is divisble by 7")'''
    
#Safe Division
'''try:
 num1=int(input("enter number one"))
 num2=int(input("enter number two"))

 result = num1 / num2
 print(result)
except ValueError:
    print("the number you entered is not integer")
except ZeroDivisionError:
    print("the number two you entered is 0 which is invalid")'''
#safefile opening
'''try :
    file=open("mudeer.txt","r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("there is no file withh name ")'''
#File Handling + Exception Handling
'''try:
    file=input("enter file name")
    filen=open(file,"r")
    print(filen.read())
    filen.close()
except FileNotFoundError:
    print("there is no such file")'''
    
#Write to a File
'''try:
    user=input("enter file you want to write")
    filen=open(user,"w")    
    
    message=input("enter message : ")
    filen.write(message)
    print("message write seccussfully")
    filen.close()
except FileNotFoundError:
    print("invsalid file name")'''
#append to a file
'''try:
    user=input("Enter file name")
    filen=open(user,"a")
    message=input("what you want to append in file")
    filen.write(message)
    print("apended seccusfuly")
    filen.close()
except:
    print("invalid file name")'''
    