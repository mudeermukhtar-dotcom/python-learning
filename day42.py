#find the unique second largest number:
'''user = str(input("enter the number : "))
list = user.split()
unique_list = []
largest = float("-inf")
second_largest = float("-inf")
for i in list:
    if i not in unique_list:
        unique_list.append(i)

for i in unique_list:
    i = int(i)
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i < largest:
        second_largest = i
print(second_largest)'''
#Write a Python program that finds the frequency of every digit in a number without using a dictionauser = input("Enter the number:")
user=str(input("enter the number"))
unique=[]
for i in user:
    if i not in unique:
     count=0
     for j in user:
        if i == j:
            count += 1
     unique.append(i)
     print(f"{i} appears {count} times")



    

