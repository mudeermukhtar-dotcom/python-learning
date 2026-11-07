#nested dictionary:
'''employees = {
    "emp1": {"name": "Ayan", "salary": 30000, "department": "IT"},
    "emp2": {"name": "Rohan", "salary": 45000, "department": "HR"},
    "emp3": {"name": "Mehak", "salary": 50000, "department": "IT"},
    "emp4": {"name": "Zoya", "salary": 35000, "department": "Finance"}
}
print("ALL EMOPLEE NAMES")
for key,value in  employees.items():   #all employee names
    print(value["name"])
    value["salary"] += 5000
    print(key,":",value["salary"])
print("EMPLOYEE THAT TAKE PART IN IT ")
for key,value in  employees.items(): #only it deparment 
    if value["department"]=="IT":
        print(value["name"])'''
#nested dictionary
'''students = {
    "s1": {"name": "Ayan", "marks": 85, "subject": "Python"},
    "s2": {"name": "Rohan", "marks": 62, "subject": "Java"},
    "s3": {"name": "Mehak", "marks": 92, "subject": "Python"},
    "s4": {"name": "Zoya", "marks": 48, "subject": "Java"},
    "s5": {"name": "Kabir", "marks": 76, "subject": "Python"}
}
for key,value in students.items():
    print("NAME : ",value["name"],"MARKS : ",value["marks"]) #prints student name and marks
    value["marks"]+=5       #adds 5 marks to each student
print("studnets who have python subject")
for key,value in students.items():
    if value["subject"]=="Python":
        print(value["name"])
print("students who have above 80 marks")
for key,value in students.items():
    if value["marks"]>= 80:
        print(value["name"])'''
#dictionary compresion
#normal method
'''squares={}
for i in range(0,6):
    squares[i]=i*i
print(squares)'''
#compresion method
'''squares = {i: i * i for i in range(1, 6)}
print(squares) ''' 
#example  2
'''students = {
    "Ayan": 85,
    "Rohan": 42,
    "Mehak": 92,
    "Zoya": 35,
    "Kabir": 76,
    "Arjun": 28
}
new_studnets={key.upper() : value+5 for key,value in students.items() if value >= 60} 
print(new_studnets)'''
#merging dictionaries
'''school1 = {
    "Ayan": 85,
    "Rohan": 70,
    "Mehak": 92
}

school2 = {
    "Zoya": 80,
    "Kabir": 75,
    "Rohan": 90
}
final_result=school1|school2
print(final_result)
print(final_result["Rohan"])
'''
#EXAMPLE 2
class_a = {"Ayan": 80, "Rohan": 75, "Mehak": 90}
class_b = {"Rohan": 85, "Zoya": 88}
class_c = {"Kabir": 70, "Mehak": 95}
final_result=class_a|class_b|class_c
print(final_result)
print("MARKS OF MEHAK",final_result["Mehak"])
print("MARKS OF ROHAN",final_result["Rohan"])
