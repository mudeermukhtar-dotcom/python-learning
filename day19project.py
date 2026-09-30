student_no = int(input("how many students you want to add"))
students_data = []
fails_l = []
passs_l = []
highest = 0
total_marks = 0
students = []


for i in range(0, student_no):
    name = input("enter name of  student")
    marks=int(input("enter the marks of student"))
    while marks < 0 or marks > 100:
        print("you entered incorrct marks")
        marks = int(input("enter the marks of student"))
    roll_no = int(input("enter roll no"))
    students_data.append(["name:", name, "roll_no :", roll_no, "marks ;", marks])
    students.append(name)
    total_marks = marks + total_marks
    average = total_marks / len(students_data)
   

    if marks <= 30:
        fails_l.append(name)
    else:
        passs_l.append(name)

    if marks > highest:
        highest = marks
        topper = name

search_roll = int(input("enter the roll number"))
for j in students_data:

    if search_roll == j[3]:
        print(j)
else:
    print("student not found")
print("THE MARKS AVERAGE IS ", average)
print("THE TOPPER OF CLASS IS", topper)
print("THE HIGHEST SCORED MARKS IN CLASS ARE", highest, "by MR.", topper)
print("PASSING STUDENTS LIST", passs_l)
print("FAILED STUDENTS LIST", fails_l)
while True:
    print("1. Add Student")
    print("2. Show All Students")
    print("3. Find Topper")
    print("4. Class Average")
    print("5. Passed Students")
    print("6. Failed Students")
    print("7. Search Student")
    print("8. Exit")
    choice = int(input("enter number"))
    if choice == 1:
        name = input("enter name of  student")
        marks=int(input("enter the marks of student"))
        while marks < 0 or marks > 100:
            print("you entered incorrct marks")
            marks = int(input("enter the marks of student"))
          
        roll_no = int(input("enter roll no"))
        students_data.append(["name:", name, "roll_no :", roll_no, "marks ;", marks])
        students.append(name)
        if marks <= 30:
            fails_l.append(name)
        else:
            passs_l.append(name)
            
        if marks > highest:
         highest = marks
         topper = name
        total_marks = marks + total_marks
        average = total_marks / len(students_data)
        

    elif choice == 2:
        print("this  is the list of al the studnets ", students_data)
    elif choice == 3:
        print("the topper of your class is :", topper)
    elif choice == 4:
        print("THE MARKS AVERAGE IS ", average)
    elif choice == 5:
        print("PASSING STUDENTS LIST", passs_l)
    elif choice == 6:
        print("FAILED STUDENTS LIST", fails_l)
    elif choice == 7:
        search_student = input("enter the name ")
        for x in students_data:
            if search_student == x[1]:
                print(x)
                break
        else:
            print("student not found")
           
    elif choice == 8:
        break
