#write a Python program that creates a Student class with name and age attributes. Create two student objects and print their names and ages
'''class students():
    name="mudeer"
    age="18"
    def info(self):
        print(f"{self.name} is {self.age} years old")
a=students()
b=students()
a.name="mudeer"
b.name="danihs"
a.age=18
b.age=12
a.info()
b.info()'''
#Write a Python program to create a Car class with brand and colour attributes. Create two objects with different values and use a show() method to display their details.
'''class car():
    colour=""
    brand=""
    def info(self):
        print({f"brand :{self.brand} , colour {self.colour}"})
c1=car()
c1.colour="black"
c1.brand="audi"
c2=car()
c2.brand="ferrari"
c2.colour="red"
c1.info()
c2.info()'''
'''#Write a Python program to create a Mobile class with brand and price attributes. Create two objects with different values and display their details using a show() method.
class mobile():
    brand=""
    price=int()
    def show(self):
        print(f"BRAND : {self.brand}, PRICE : {self.price}")
m1=mobile()
m1.brand="redmi"
m1.price=2000
m2=mobile()
m2.brand="iphone"
m2.price= 10000
m1.show()
m2.show()'''
#Write a Python program to create a RailwayTicket class with the following attributes:
'''class RailwayTicket():
    name=""
    train=""
    price=int()
    def show(self):
        print(f"NAME : {self.name}\nTRAIN : {self.train} \nPRICE : {self.price} ")
r1=RailwayTicket()
r1.name="MUDEER" 
r1.train="VANDE BHARAT EXPRESS"
r1.price=1500
r2=RailwayTicket()
r2.name="DANISH"
r2.train="MUMBAI EXPRESS"
r2.price=3000
r1.show()
r2.show()'''

#Write a Python program to create an Employee class with a constructor that accepts name, age, and salary.
#Create two employee objects with different values and display their details using a show() method.
'''class Employee():
    def __init__(self,n,a,s):
        self.name=n
        self.age=a
        self.salary=s
    def show(self):
        print(f" HI I AM {self.name} having age {self.age} age with salary{self.salary}.")
a=Employee("mudeer",18,20000)
b=Employee("danish",32,450000)
a.show()
b.show()
'''
#rite a Python program to create a BankAccount class with a constructor that accepts account_holder and balance
# . Create two objects with different values and display their details using a show() method.
class bankaccount():
    def __init__(self,n,b):
        self.name=n
        self.balance=b
    def show(self):
        print(f"NAME : {self.name} BALANCE : {self.balance}")
        
a=bankaccount("mudeer",32222)
b=bankaccount("danish",450000)
a.show()
b.show()