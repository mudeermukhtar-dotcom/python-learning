#Write a Python program that uses a decorator to print Before function before a function runs and After function after it runs.
'''def decorates(func):
    def bf():
        print("before function")   
        func() 
        print("after function")
    return  bf
@decorates
def world():
    print("hello words")
world()'''
#Write a Python program that uses a decorator to print Login successful before executing a function and Thank you after executing it.  
'''def greeting(func):
    def bf():
        print("login successfull")
        func()
        print("thankyou") 
    return bf
@greeting
def pade():
    print("wwelcome to dashboard")
pade()'''
#greet after and before sum
'''def function(func):
    def greet(a,b):
     print("function is starting") 
     func(a,b)
     print("funcion has ended")  
    return greet
@function
def sum(a,b):
    print("sum = ",a+b)
sum(20,20)'''
#example 
'''def function(func):
    def greet(*args,**kwargs):
     print("function is starting") 
     func(*args,**kwargs)
     print("funcion has ended")  
    return greet
@function
def sum(a,b):
    print("sum = ",a+b)
sum(20,20)
@function
def sub(c,d):
    print("sum = ",c-d)
sub(30,20)'''
#example
'''def function(c):
    def greet():
        print("hii")
        c()
        print("byy")   
    return greet   

def hii():
    print("ppppp")
    
function(hii)()'''
      

#example :
'''def function(func):
    def fx():
        print("function started ")
        func()
        print("function ended")
    return fx
@function
def main():
    print("welcome to python")
main()'''
#example 
'''def my_decorater(func):
    def greeting():
        print("function started ...")
        func()
        print("function ended")
    return greeting
@my_decorater
def sum():
    a=int(input("enter the number"))
    b=int(input("enter the number"))
    print(a+b)
sum()'''
#example 
'''def my_decorater(func):
    def greeting():
        print("function started ...")
        func()
        print("function ended")
    return greeting
@my_decorater
def sum():
    a=int(input("enter the number"))
    b=int(input("enter the number"))
    print(a+b)
sum()
@my_decorater
def sub():
    c=int(input("enter the number "))
    d=int(input("enter thenumber "))
    print(c+d)
sub()'''
#example
'''def my_decorater(func):
    def greet(*args,**kwargs):
        print("welcome")
        func(*args,**kwargs)
        print("thankyou")
    return greet
@my_decorater
def sum(a,b):
    print(a+b)
sum(10,20)'''