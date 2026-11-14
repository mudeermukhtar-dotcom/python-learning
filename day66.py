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
'''class bankaccount():
    def __init__(self,n,b):
        self.name=n
        self.balance=b
    def show(self):
        print(f"NAME : {self.name} BALANCE : {self.balance}")
        
a=bankaccount("mudeer",32222)
b=bankaccount("danish",450000)
a.show()
b.show()'''