#SOME EXAMPLES OF GLOBAL
#1.
'''x=85
def marks():
    global x
    print(x) 
marks()
'''
#2.
'''balance=5000
def deposit():
    global balance
    balance = balance + 1000
    print(balance)
deposit()'''
#3.
'''score=0
def increase_function():
    global score
    score=score+1
increase_function() 
increase_function() 
increase_function() 
   
print(score)'''
#--------OR--------
'''score=0
def increase_function():
    global score
    score=score+1
for i in range(0,3):
    increase_function()
   
print(score)'''
#4.
score=0
def increase_score(score):
    
    score=score+1
    return score
for i in range(0,3):
    score=  increase_score(score)
print(score)
    
