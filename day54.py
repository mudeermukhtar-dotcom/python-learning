'''#q1 
## Question 9 — Student Records Analysis

Write a Python program using this list of tuples:

students = [
    ("Mudeer", 18, 85),
    ("Ali", 19, 72),
    ("Rahul", 18, 91),
    ("Ayaan", 20, 45),
        ("Zoya", 19, 85)
]
Your program must:

1. Print the name and marks of every student.
2. Find the highest marks without using `max()`.
3. Count how many students scored 85 marks.
4. Create a new list containing the names of students who scored 80 or more.
5. Print the names in that new list.
#sol
students = [
    ("Mudeer", 18, 85),
    ("Ali", 19, 72),
    ("Rahul", 18, 91),
    ("Ayaan", 20, 45),
    ("Zoya", 19, 85)
]
new_list=[]
highest=0
count=0
for student in students:
    if student[2]> highest:
        highest=student[2]
    if student[2] == 85:
        count +=1
    if student[2] >= 80:
        new_list.append(student[0])
    
    print(f"NAME : {student[0]}    | MARKS : {student[2]}" )
print(f"THE NUMBER OF STUDENT THAT HAVE SCORED 85 MARKS ARE {count}")
print("THESE ARE STUDNET THAT HAVE SCORED AVBOVE 80"," ".join(new_list))
print("highest marks ",highest)'''

#Q2
'''students = [
    ("Mudeer", (85, 90, 78)),
    ("Ali", (65, 72, 80)),
    ("Rahul", (92, 88, 95)),
    ("Ayaan", (35, 40, 45)),
    ("Zoya", (76, 82, 89))
]


### Tasks
Calculate the total marks of each student without using the sum() function.

Calculate and print the average marks of each student.

Find the student with the highest average without using the max() function.

Store the names of students whose average is greater than or equal to 80 in a new list.

At the end, print:

The highest average.

The name of the student with the highest average.

The names of students whose average is greater than or equal to 80.
#SOL
students = [
    ("Mudeer", (85, 90, 78)),
    ("Ali", (65, 72, 80)),
    ("Rahul", (92, 88, 95)),
    ("Ayaan", (35, 40, 45)),
    ("Zoya", (76, 82, 89))
]
marks_list=[]
average_list=[]
student_name=[]
good_names=[]
highest=0
for student in students:
    total=0
    for j in student[1]:
        total +=j
    average=total/3
    if average >= 80:
        good_names.append(student[0])
    student_name.append(student[0])
   
    average_list.append(average)
    marks_list.append(total)
for x in average_list:
    if x > highest:
        highest=x
index=average_list.index(highest)
print("====================================================================")
print("THE STUDENTS WHOOSE AVEARGE IS  ABOVE 80 ARE ",", ".join(good_names))
print(f"{student_name[index]} has {average_list[index]} average marks in the class")
'''
#q3
'''Question 11: Subject-wise Student Analysis
students = [
    ("Mudeer", (85, 90, 78)),
    ("Ali", (65, 72, 80)),
    ("Rahul", (92, 88, 95)),
    ("Ayaan", (35, 40, 45)),
    ("Zoya", (76, 82, 89))
]

subjects = ("English", "Maths", "Science")
### Tasks
1. Print each student's name and marks in all three subjects.
2. Print `PASS` if a student scores 40 or more in a subject; otherwise, print `FAIL`.
3. Count the total number of students who scored below 40 in at least one subject.
4. Find the highest marks in each subject without using `max()`.
5. Print the subject name and its highest marks.'''

students = [
    ("Mudeer", (85, 90, 78)),
    ("Ali", (65, 72, 80)),
    ("Rahul", (92, 88, 95)),
    ("Ayaan", (35, 40, 45)),
    ("Zoya", (76, 82, 89))
]

subjects = ("English", "Maths", "Science")

count = 0
highest_marks = [0, 0, 0]

for student in students:
    print("NAME:", student[0])

    for i in range(len(student[1])):
        marks = student[1][i]

        if marks >= 40:
            result = "PASS"
        else:
            result = "FAIL"

        print(f"{subjects[i]}: {marks} - {result}")

    print("==============================")


for student in students:
    for marks in student[1]:
        if marks < 40:
            count += 1
            break

print("Students with at least one subject below 40:", count)
for student in students:
    for i in range(len(student[1])):
        if student[1][i] > highest_marks[i]:
            highest_marks[i] = student[1][i]

print("\nHIGHEST MARKS IN EACH SUBJECT:")

for i in range(len(subjects)):
    print(f"{subjects[i]}: {highest_marks[i]}")

       

         
         