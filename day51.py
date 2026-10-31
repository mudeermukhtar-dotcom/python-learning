#FIND SECOND LARGEST:
'''user=input("enter the list of numbers").split()
largest=float('-inf')
second_largest=float('-inf')
for i in user:
    i=int(i)
    if i > largest :
        second_largest=largest
        largest=i
    elif i > second_largest and i < largest :
        second_largest=i
if second_largest == float('-inf'):
    print("second largest does not exist")
else:
    print(second_largest)'''
#DUPLICATE NUMBERS REMOVE:
'''user=input("enter the list of numbers : ").split()
new_list=[]
for i in user :
    if i not in new_list:
        new_list.append(i)
print(new_list)'''
#DIGIT FREQUENCY
user=input("enter the list of numbers : ").split()
countl=[]
new_list=[]
largest=float('-inf')
for i in user:
    count=0
    for j in user:
        if i == j :
            count=count+1
    

    if i not in new_list:
     new_list.append(i)
     countl.append(count)
for z in range(len(countl)):
    z=int(z)
    
    if countl[z] > largest:
        largest=countl[z]
        index=z
if largest == 1:
    print("All numbers have the same frequency")
else:
    print("The first most frequent number is", new_list[index])
  
