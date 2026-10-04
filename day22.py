#Ask the user to enter a student name. Then search for that student in the dictionar
'''students = {
    "Mudeer": 85,
    "Ayaan": 72,
    "Rahul": 45,
    "Zaid": 91,
    "Arman": 88
}
user=str(input("enter the name"))
if user in students:
    print(students.get(user))
else:
    print("student not found")'''
#Write a Python program to print the names of students who failed.
'''students = {
    "Mudeer": 85,
    "Ayaan": 72,
    "Rahul": 45,
    "Zaid": 91,
    "Arman": 88
}
fail=[]
pas=[]
for name , marks in students.items():
    if marks < 50 :
        fail.append(name)
    elif marks > 50 :
        pas.append(name)
print(fail)
print(pas)'''
#Find the name of the student who scored the highest marks.
'''students = {
    "Aarav": 67,
    "Kabir": 94,
    "Rohan": 81,
    "Dev": 76,
    "Arjun": 89
}
highest=0
second_highest=0
for name , marks in students.items():
    if marks > highest:
        second_highest=highest
        topper2=name
        highest=marks
        topper=name
     
        
    elif marks > second_highest and  marks < highest:
      second_highest=marks
      topper2=name
        
print(second_highest,topper2)'''
#Write a Python program to find the class average and then count how many students scored above the:
''''students = {
    "Aarav": 67,
    "Kabir": 94,
    "Rohan": 81,
    "Dev": 76,
    "Arjun": 89
}
total=0
count=0

for marks in students.values(): 
    total += marks
average=total/len(students)
for  marks in students.values():
    if marks > average:
        count=count+1
print(f"{count} students have scored anove {average} marks")'''
#Find the student whose marks are closest to the class averag
'''students = {
    "Aarav": 67,
    "Kabir": 94,
    "Rohan": 81,
    "Dev": 76,
    "Arjun": 89
}
total=0
for marks in students.values():
    total += marks
average=total/len(students)
diffrence=float('+inf')
for name, marks in students.items():
    if abs(average-marks) < diffrence:
        diffrence=abs(average-marks)
        close_name=name
        close_marks=marks
print(f"{close_name} has {diffrence:.2f} near the average and he has scored {close_marks}")'''
#: Find and print the names of all students who scored below the class average.
'''students = {
    "Aarav": 67,
    "Kabir": 94,
    "Rohan": 81,
    "Dev": 76,
    "Arjun": 89
}
total=sum(students.values())
average=total/len(students)
list=[]
for name, marks in students.items():
    if marks < average :
        list.append(name)
print(f"{list} have scored below {average}" )'''

    
     
