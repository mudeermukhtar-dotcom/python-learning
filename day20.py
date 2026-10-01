#write a Python program to print all the keys of the dictionary.
'''student = {
    "name": "Mudeer",
    "age": 18,
    "course": "CSE"
}
print(student.keys())'''
#write a Python program to print all the values of the dictionary.
'''student = {
    "name": "Mudeer",
    "age": 18,
    "course": "CSE"
}
print(student.values())'''
#Write a Python program to print all key-value pairs of the dictionary.
'''student = {
    "name": "Mudeer",
    "age": 18,
    "course": "CSE"
}
print(student.items())'''
#Write a Python program to print the student's name using get() method.
'''student = {
    "name": "Mudeer",
    "age": 18,
    "course": "CSE"
}
print(student.get("name"))'''
#Write a Python program to change the student's age from 18 to 19 using the update() method.
'''student = {
    "name": "Mudeer",
    "age": 18,
    "course": "CSE"
}
student.update({
    "age":19
})
print(student)
'''
#Remove the "age" key-value pair using the pop() method
'''student = {
    "name": "Mudeer",
    "age": 18,
    "course": "CSE"
}
student.pop("age")
print(student)'''
#: Use get() to print the name and course.
'''student = {
    "name": "Mudeer",
    "age": 18,
    "course": "CSE"
}
x=student.get("name")
y=student.get("course")
print(x,y)'''
#Add a new key "marks" with value 85 to the dictionary using update()
'''student = {
    "name": "Mudeer",
    "age": 18,
    "course": "CSE"
}
student.update({
    "marks":85
})
print(student)'''
#Remove "course" from the dictionary using pop() and then print the updated dictionary.
'''student = {
    "name": "Mudeer",
    "age": 18,
    "course": "CSE"
}
print(student.pop("course"))'''
#Change "age" to 19 using update()
#Print the updated "age" using get()
'''student = {
    "name": "Mudeer",
    "age": 18,
    "course": "CSE"
}
student.update({
    "age":19
})
print(student.get("age"))'''
#Print all keys using keys()
#Print all values using values()
'''student = {
    "name": "Mudeer",
    "age": 18,
    "course": "CSE"
}
print(student.keys())
print(student.values())'''
#Dictionary ke saare key-value pairs print karo using items():
'''student = {
    "name": "Mudeer",
    "age": 18,
    "course": "CSE"
}
print(student.items())'''
#Check karo ki dictionary mein "marks" key hai ya nahi.
student = {
    "name": "Mudeer",
    "age": 18,
    "course": "CSE"
}
if "marks" in student:
    print("yes")
else:
    print("no")