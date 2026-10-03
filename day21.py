#Write a Python program to print the name and marks of the student:

'''student = {
    "name": "Mudeer",
    "age": 18,
    "course": "CSE",
    "marks": 85
}
print(student.get("marks"),student.get("name"))'''

#Write a Python program to check whether the "marks" key is present in the dictionary.
'''student = {
    "name": "Mudeer",
    "age": 18,
    "course": "CSE",
    "marks": 85
}
if "marks" in student:
    print("yes")
else:
    print("no")'''

#Write a Python program to change the marks from 85 to 90 using the update() method.
'''student = {
    "name": "Mudeer",
    "age": 18,
    "course": "CSE",
    "marks": 85
}
student.update({"marks":90})
print(student)'''
#Write a Python program that uses a loop to print the names of students who scored 80 or more marks.
'''students = {
    "Mudeer": 85,
    "Ayaan": 72,
    "Rahul": 45,
    "Zaid": 91
}
for name,marks in students.items():
    if marks >= 80:
        print(name)
        '''
#Write a Python program to calculate the total marks of all students using a for loop.
'''students = {
    "Mudeer": 85,
    "Ayaan": 72,
    "Rahul": 45,
    "Zaid": 91
}
total=0
for name , marks in students.items():
    total += marks
print(total)'''
#Write a Python program using a for loop to find the student with the highest marks.
'''students = {
    "Mudeer": 85,
    "Ayaan": 72,
    "Rahul": 45,
    "Zaid": 91
}
highest=0
for name,marks in students.items():
    if  marks > highest:
        highest = marks
        topper= name
print(name,marks)'''
#Write a Python program using a for loop to count how many students scored 80 or more.
'''students = {
    "Mudeer": 85,
    "Ayaan": 72,
    "Rahul": 45,
    "Zaid": 91,
    "Arman": 88
}
count=0
for name,marks in students.items():
    if marks > 80:
        count=count+1
print(count)'''
#Write a Python program using a for loop to calculate the average marks of all students.

'''students = {
    "Mudeer": 85,
    "Ayaan": 72,
    "Rahul": 45,
    "Zaid": 91,
    "Arman": 88
}
total=0
for name , marks in students.items():
    total += marks
print(total)
print(total/len(students))'''
#Write a Python program using a for loop to find the student with the lowest marks.
'''students = {
    "Mudeer": 85,
    "Ayaan": 72,
    "Rahul": 45,
    "Zaid": 91,
    "Arman": 88
}
lowest=float('+inf')
for name , marks in students.items():
    if  marks < lowest:
        lowest=marks
        topper=name
print(topper,lowest)
'''