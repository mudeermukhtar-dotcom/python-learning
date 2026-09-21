#Find the second largest number in a list by using if and for loop:
'''''
numbers = [12, 45, 7, 89, 34, 67]
largest=numbers[0]
largest1=numbers[0]
for i in numbers:
    if i > largest:
        largest=i
for i in numbers: 
 if i > largest1 and i < largest:
     largest1=i
print("second largest number is ",largest1)'''''
#Find the second smallest number in a list without using
''''
numbers = [25, 12, 8, 31, 6, 19]
smallest=numbers[0]
smallest1=numbers[0]
for i in numbers:
    if i < smallest:
        smallest=i
for i in numbers:
    if i < smallest1 and i > smallest:
      smallest1=i
print("second smallest number is ",smallest1)'''''
#Find the largest difference between any two numbers in the list.
'''numbers = [10, 4, 18, 7, 25, 12]
largest=numbers[0]
smallest=numbers[0]
for i in numbers:
    if i > largest:
        largest=i
for i in numbers:
    if i < smallest:
        smallest=i
largestdiff=largest-smallest
print("the largest diffrence in the list",largestdiff)'''
#Count how many numbers are greater than the average of the list.
'''numbers = [10, 20, 30, 40, 50]
total=sum(numbers)
length=len(numbers)
average=total/length
count=0
for i in numbers:
    if i > average:
        count=count+1
print("the toal numbers which are greater then the average",count)'''
#Find the number that appears most frequently in the list.
'''numbers = [2, 5, 3, 2, 8, 5, 2, 9, 5, 5]
count=0
for i in numbers:
    count=0
    for j in numbers:
        if i == j:
            count=count+1
print("the most appearing in the list is ",j)
print("it appears",count,"times inn the given list")'''
#Take password from user untill user will tell the coorect password:

'''i=int(input("enter password"))
password=1234

while i != password:
   if i != password:
    print("you entered incoorect")
    i=int(input("enter password"))
if i == password:
 print("you entered corect")'''
#Find the first number in the list that appears more than once.
'''numbers = [4, 7, 2, 9, 7, 5,  2,]
for i in numbers:
    count=0
    for j in numbers:
        if i == j:
         count=count+1

    if count > 1: 
     print(i)
     break
print(i,"comes ",count,"times in a list")
print(" first number in the list that appears more than once is",i)'''
#Write a Python program to create a new list containing only unique numbers:
'''numbers = [4, 7, 2, 9, 7, 5, 2, 4]
new_list=[]
for i in numbers:
    if i  not in new_list:
     new_list.append(i)

print(new_list)'''
#Write a Python program to create a new list containing the numbers that are present in both lists.
'''numbers1 = [4, 7, 2, 9, 5]
numbers2 = [8, 2, 7, 6, 5]
newlist=[]
for j in numbers1 :
 for i in numbers2:
        if i ==j:
    
         newlist.append(i)
print(newlist)'''
#Python program to find the missing number from a list containing numbers from 1 to 6.
'''numbers = [1, 2, 3, 5, 6]
newlist=[]
i=1
while i <= 6:
    newlist.append(i)
    i=i+1

for i in newlist:
    if i not in numbers:
     print("the missing numbers is numbers is",i)
     break'''


        


    








