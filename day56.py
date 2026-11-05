#DICTIONARIES
#example
'''student = {
    "name": "Ali",
    "age": 18,
    "marks": 420
}
print(student["name"])
print(student["marks"])
student.update({"age" : 20})
print(student)
print(student.get("age")) '''   #does not give eerror if not present
#

'''students = {
    "Ali": 78,
    "Rahul": 92,
    "Aman": 65,
    "Zoya": 88,
    "Sara": 92
}
highest=0
total=0
for key,vlaue in students.items():
  print("marks :",vlaue)
  total=total+vlaue
  if vlaue > highest:
    highest=vlaue
    name=key
for key,vlaue in students.items():
  if vlaue == highest:
    name=key
    print(f"{name} has scored {vlaue}")
    
print(total/5)'''
#
'''students = {
    "Ali": 78,
    "Rahul": 92,
    "Aman": 35,
    "Zoya": 88,
    "Sara": 42,
    }
fail_count=0
pass_count=0
for key,value in students.items():
  if value > 50:
    print(f"{key}: pass")
    pass_count+=1
  else:
    print(f"{key}:fail")
    fail_count+=1
print("pass count",pass_count)
print("FAIL COUNT",fail_count)'''

#
'''students = {
    "Ali": 78,
    "Rahul": 92,
    "Aman": 65,
    "Zoya": 88,
    "Sara": 85
}
highest=0
second_highest=0
highest_name=""
second_highest_name=""

for key,value in students.items():
  if value > highest:
    second_highest=highest
    second_highest_name=highest_name
    highest=value
    highest_name=key
  elif value > second_highest and value < highest:
    second_highest_name=value
    name=key
    
print(f"{second_highest_name} is the 2nd topper of class has scored {second_highest}")'''
'''#MAKE NEW DICTIONARY TO COUNT PASS AND FAIL
students = {
    "Ali": 78,
    "Rahul": 92,
    "Aman": 35,
    "Zoya": 88,
    "Sara": 42,
    "Usman": 29,
    "Riya": 65
}
new={}
pass_count=0
fail_count=0
for key,value in students.items():
  if value >= 50:
    pass_count+=1
    
  else:
    fail_count+=1
new["pass"]=pass_count
new["fail"]=fail_count
print(new)'''
#
'''prices = {
    "Laptop": 50000,
    "Phone": 25000,
    "Headphones": 2000,
    "Mouse": 800
}
expensice={}
for key,value in prices.items():
  if value > 5000:
    expensice[key]=value
print(expensice)
    '''
#
'''students = {
    "Ali": 78,
    "Rahul": 92,
    "Aman": 65,
    "Zoya": 88,
    "Sara": 85
}
highest=0
for key,value in students.items():
  if value > highest:
    highest=value
    name=key
print("NAME : ",name) 
print("MARKS : ",highest) '''
#
'''students = {
    "Ali": 78,
    "Rahul": 92,
    "Aman": 65,
    "Zoya": 88,
    "Sara": 85
}
above={}
total=0
for key,value in students.items():
  total += value
average=total/len(students)
for key,value in students.items():
  if value > average:
    above[key]=value
print(above)
'''
#
'''students = {
    "Ali": 78,
    "Rahul": 92,
    "Aman": 65,
    "Zoya": 88,
    "Sara": 85
}
good={}
for key,value in students.items():
  if value >= 80:
    good[key]=value
print(good)
  '''
#
products = {
    "Laptop": 50000,
    "Phone": 25000,
    "Mouse": 800
}
products.update({"phone":2700,"keyboard":5000})
print(products)

    
  