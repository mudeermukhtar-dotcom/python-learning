# Duplicate Marks Finder
'''students = {
    "Ayan": 90,
    "Rohan": 85,
    "Mehak": 90,
    "Zaid": 70,
    "Sara": 85,
    "Kabir": 60,
    "Riya": 90,
}
list = []
duplicate_list = []
find = {}
for key, value in students.items():
    list.append(value)
for i in list:
    count = 0
    for key, value in students.items():
        if i == value:
            count += 1
    if count > 1 and i not in duplicate_list:
        duplicate_list.append(i)

for j in duplicate_list:
 for key,value in students.items():
     if j ==  value:
         find[key]=value
print(find)'''
#duplicate value items:
'''products = {
    "Laptop": 50000,
    "Phone": 25000,
    "Tablet": 30000,
    "Monitor": 25000,
    "Keyboard": 1500,
    "Mouse": 1500
}
price=[]
duplicate=[]
dict={}
for key,value in products.items():
    price.append(value)
for i in price:
    count=0
    for key,value in products.items():
        if i == value:
            count +=1
    if count > 1 and i  not in  duplicate:
        duplicate.append(i)
for j in duplicate:
    for key,value in products.items():
        if j == value:
            dict[key]=j
print(dict)'''

#PRINT SECOND LARGEST NUMBER :
'''new_dictionary={}
largest=0
second_largest=0
largest_name=""
second_largest_name=""

students = {
    "Ayan": 90,
    "Rohan": 85,
    "Mehak": 90,
    "Zaid": 70,
    "Sara": 95,
    "Kabir": 60,
    "Riya": 85
}
new_dictionary={}
largest=0
largest_name=""
second_largest=0
second_largest_name=""
for key,value in students.items():
    if value > largest:
        second_largest_name=largest_name
        second_largest=largest
        largest_name=key
        largest=value
    elif value >= second_largest and value < largest:
        second_largest=value
        second_largest_name=key
for key, value in students.items():
    if value == second_largest:
        new_dictionary[key] = value

print(new_dictionary)'''
#department system analysis
'''employees = {
    "Ayan": 45000,
    "Rohan": 60000,
    "Mehak": 75000,
    "Zaid": 45000,
    "Sara": 90000,
    "Kabir": 60000,
    "Riya": 80000
}
new_dictionary={}
total=0

for key,value in employees.items():
    total += value 
average=total/len(employees)  
for key,value in employees.items():
    if value > average:
        new_dictionary[key]=value
print(new_dictionary)'''
#product price analysis
'''products = {
    "Laptop": 50000,
    "Phone": 25000,
    "Tablet": 30000,
    "Monitor": 25000,
    "Keyboard": 1500,
    "Mouse": 1500,
    "Camera": 40000
}
above_average={}
second_highest_dict={}
total=0
highest=0
second_highest=0
highest_name=""
second_highest_name=""
for key,value in products.items():
    total += value
average=total/len(products)
for key,value in products.items():
    if value > average:
        above_average[key]=value
for key,value in products.items():
    if value > highest:
        
        second_highest=highest
        highest=value
    
    elif value > second_highest and value < highest:
        second_highest=value
for key,value in products.items():
    if value == second_highest:
        second_highest_dict[key]=value
print("above average : ",above_average)
print(second_highest_dict)'''
#nested dictionary
employees = {
    "emp1": {
        "name": "Ayan",
        "salary": 30000
    },
    "emp2": {
        "name": "Rohan",
        "salary": 45000
    },
    "emp3": {
        "name": "Mehak",
        "salary": 50000
    }
}

      
        
    
print(employees["emp1"]["salary"])
print(employees["emp2"]["name"])