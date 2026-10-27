#Write a Python program that uses a decorator to print Good Morning before a function runs and Have a nice day after it runs.
'''def goodday(func):
    def greet():
        print("good morning")
        func()
        print("have a nice day")
    return greet
    
@goodday
def  main():
    print('welcome to python')
main()
'''
#Write a Python program using a decorator that prints "Good Morning" before a function runs and "Have a nice day" after it runs.
'''def add(func):
    def grret(a,b):
        print("good morning")
        func(a,b)
        print("have a nice day")
 
    return grret
@add
def main(a,b):
    sum=a+b
    print(sum)
main(10,20)'''
#write a Python program using a decorator that prints "Starting..." before a function runs and "Finished!" after it runs; the function should print "Hello Python!".
'''def decorater(func):
    def greet():
        print("starting")
        func()
        print("finished")
    return greet
@decorater
def main():
    print("hii python")
main()
        '''
#Write a Python program to create a Student class with name and age attributes, create an object, and display the student's details.
'''class students():
    name=""
    age=0
    def info(self):
        print(f"{self.name}:{self.age}")
a=students()
b=students()
a.age=18
a.name="mudeer"
a.info()
b.name="danish"
b.age=122
b.info()
'''
#Write a Python program to create a `Student` class using `__init__()` to initialize `name` and `marks`, then create two objects and display their details.
'''class students():
    name=""
    marks=int()
    
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def show(self):
         print(f"NAME {self.name} :  MARKS {self.marks}")
a=students("mudeer",19)
b=students("danish",29)
a.show()
b.show()'''
#getter and setters
#exampl1 
'''class student:
    def __init__(self,name):
        self.name=name
    @property
    def main(self):
        print(f"i am {self.name}")
        return self.name
    @main.setter
    def main(self,newname):
        self.name=newname



a=student("mudeer")
print(a.main)       
a.main = "Danish" 
print(a.main)   '''    

