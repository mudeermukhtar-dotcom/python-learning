#check wheter the number is armstrong or not?
'''n = int(input("enter the number : "))
length=len(str(n))
original_number=n
sum=0
while n > 0:
    total=(n%10)**length
    sum=sum+total
    n=n//10
if sum == original_number:
    print("the number is armstrong")
else:
    print("the number is not armstrong")''' 
#finally keywords
'''try:
 num1=int(input("enter first number"))
 num2=int(input("enter second number"))
 result=num1/num2
 print(result)
except ZeroDivisionError:
    print("number cant be divided by zero")
except ValueError:
    print("the number cant be integer")
finally:
    print("program finished")'''
#file handling
'''try:
 file_name=input("enter file name")
 file=open(file_name,"r")
 print(file.read())
 file.close()
except FileNotFoundError:
    print("the file does not exist")
finally:
    print("file operation successfully")'''
#Custom Exception
'''class invalidageerror(Exception):
    pass
try:
    age=int(input("enter your age"))
    if age < 0 or age > 100:
        raise invalidageerror
        

    if age >= 0 and age <= 18:
        print("you cant vote")
    else:
        print("you can vote")
except ValueError:
    print("age cant be in alphabets")
except invalidageerror:
    print("age is invalid")'''
#Invalid Marks
'''class invalid_marks(Exception):
 pass
try:
     marks=int(input("enter marks"))
     if marks > 100 or marks < 0:
         raise invalid_marks
     if marks > 50:
      print(f"you have scored {marks} in your class you are pass")
     else:
         print("you are fail")
except ValueError:
     print("marks should be in numbers")
except   invalid_marks:
     print("you entered invalid marks")  '''
#InsufficientBalanceError
'''class InsufficientBalanceError(Exception):
    pass
class negativeError(Exception):
     pass 
   
balance=5000
try:
    user=int(input("enter withdrawl amout"))
    
    if user > balance :
        raise InsufficientBalanceError
    elif user < 0:
        raise negativeError
    elif user >=0 and user <= 5000:
        balance=balance - user
        print(f"transiction successfull.Remaining balance;{balance}")
except InsufficientBalanceError:
    print("insufficient balance in your account")
except ValueError:
    print("invalid amout")
except negativeError:
    print("you have entered amout in negatuve")'''
