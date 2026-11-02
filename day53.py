'''#tuple
#Question 1: Student Marks Analyzer
marks = (90, 75, 90, 60, 85)
total=0
largest=0
count=0
for i in marks:
    total += i
    if i > largest:
     largest=i
    if i == 90:
        count=count+1        
   
print("TOTAL MARKS",total)
print("HIGEHST MARKS ",largest)
print("90 marks scored by",count,"students")'''
#question 2:
'''student = ("Mudeer", 18, "CSE")
name,age,steam=student
print(name)
print(age)
print(steam)
if age >= 18:
    print("true")
else:
    print("false") 
'''
#QUESTION 3DATA ANALYSER
'''numbers = (12, 5, 8, 12, 3, 5, 12, 9, 4)
total=0
largest=float('-inf')
smallest=float('+inf')
count=0
even_number=()
for i in numbers:
    
    total += i
    if i > largest:
        largest=i
    if i < smallest:
        smallest=i
    if i == 12:
        count +=1
    if i % 2  == 0:
        even_number = even_number + (i,)
        
print("TOTAL SUM :",total)
print("LARGEST ",largest)
print("SMALLEST :",smallest)
print("FREQUENCY OF 12 :",count)
print(even_number)'''
#Indexing + Slicing
'''numbers = (10, 20, 30, 40, 50, 60, 70, 80)
print(f"FIRST NUMBER :{numbers[0]}")
print(f"LAST NUMBER :{numbers[-1]}")
print(f"LAST THREE NUMBERS :{numbers[-3:]}")
print(f"FIRST FOUR NUMBERS :{numbers[0:4]}")
print(f"REVRSE ORDER : {numbers[::-1]}")
print(f"EVERY SECOND ELEMENT{numbers[0::2]}")
'''
#Question 5: Student Data Manager
'''student = ("Mudeer", 18, "CSE", 85)
name,age,stream,marks=student
print("NAME : ",name)
print("AGE  : ",age)
print("BRANCH : ",stream)
print("MARKS: ",marks)
if marks > 50:
    print("YOU ARE PASSED")
else:
    print("FAIL")
updated=(student[-1],student[1],student[2],student[0])
print("NEW TUPLE",updated)'''
#quesition 6 :tuple slicing challange
'''numbers = (5, 10, 15, 20, 25, 30, 35, 40, 45, 50)
print(numbers[2:7])
print(numbers[-4:])
print(numbers[1::2])
print(numbers[::-1])'''
#question 7:tuple methods
'''numbers = (10, 20, 10, 30, 10, 40, 20)
print(numbers.count(10))
print(numbers.index(20))
print(50 in numbers)'''
#question 8:
'''numbers = (4, 7, 2, 9, 6, 3, 8, 1, 5)
new_numbers=()
odd_numbers=()
for i in numbers:
    if i > 5:
        new_numbers=new_numbers + (i,)
for j in numbers:
    if j % 2 != 0:
        odd_numbers=odd_numbers + (i,)
        
print(f"the numbers greater than 5 are ",new_numbers)
print(f"the numbers which are odd",odd_numbers)
print("total numbers that are  greater than 5",len(odd_numbers))'''
#tuple in list:
'''
students = [
    ("Mudeer", 18, 85),
    ("Ali", 19, 72),
    ("Rahul", 18, 91),
    ("Ayaan", 20, 45)
]
for i in students:
 print(f"NAME :{i[0]}")
 print(f"AGE :{i[1]}")
 print(f"MARKS :{i[2]}")

 print("===============")'''
# STUDENT RESULT ANALYSIS SYSTEM

'''students = [
    ("Mudeer", 18, (85, 90, 78)),
    ("Ali", 19, (65, 72, 80)),
    ("Rahul", 18, (92, 88, 95)),
    ("Ayaan", 20, (35, 40, 45)),
    ("Zoya", 19, (76, 82, 89))
]

high_average_students = []
passed_count = 0

highest_total = 0
top_student = ""

for student in students:
    total = 0

    # Calculate total marks
    for marks in student[2]:
        total += marks

    # Calculate average after the inner loop
    average = total / 3

    # Check PASS or FAIL
    if average >= 40:
        result = "PASS"
        passed_count += 1
    else:
        result = "FAIL"

    # Students whose average is greater than 80
    if average > 80:
        high_average_students.append(student[0])

    # Find student with the highest total
    if total > highest_total:
        highest_total = total
        top_student = student[0]

    print(f"NAME: {student[0]}")
    print(f"AGE: {student[1]}")
    print(f"TOTAL MARKS: {total}")
    print(f"AVERAGE: {average:.2f}")
    print(f"RESULT: {result}")
    print("---------------------------")

print("STUDENTS WITH AVERAGE ABOVE 80:", high_average_students)
print("TOTAL STUDENTS PASSED:", passed_count)
print("HIGHEST TOTAL:", highest_total)
print("TOP STUDENT:", top_student)'''
#diamond
'''user=int(input("enter number"))
for i in range(1,user+1):
    for j in range(user-i):
        
      print(" ",end="")
    for k in range(0,2*i-1):
      print("*", end="")
    print()
   
for l in range(user,0,-1):
    for k in range(0,user-l):
        print(" ",end="")
    for m in range(2*l-1):
        print("*",end="")
    print()'''
#factroial
'''a=int(input("enter the nuber "))
fact=1
while a > 0:
        fact=fact * a
        a=a-1
print(fact)'''
#pprime number:
'''try:
 n=int(input("enter the number: "))
except ValueError:
    print("error")
    n=int(input("enter the number :"))
count=1
for i in range(2,n+1):
    if n% i ==0:
        count += 1
    else:
        continue
if n == 1:
    print("1 is not a prime number")
if count == 2:
    print(f"{n} is a prime number ")
else:
    print("not a prime number")'''
      



    