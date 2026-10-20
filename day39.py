# find second largest

"""numbers = [12, 5, 8, 2, 15, 5, 7]
highest_number=float('-inf')
second_highest=float('-inf')
for i in numbers:
    if i > highest_number:
        second_highest=highest_number
        highest_number=i
    elif second_highest < i and i < highest_number:
        second_highest=i
print(second_highest)"""

# find second smallest
"""user=str(input("enter the list of numbers"))
numbers=user.split()
higest_small=float('+inf')
second_small=float('+inf') 
for i in numbers:
    i=int(i)
    if i < higest_small:
        second_small=higest_small
        higest_small=i
    elif i < second_small and i > higest_small:
        second_small=i
print(second_small)"""
# Remove duplicate numbers
"""user=str(input("enter the list of numbers"))
list=user.split()
new_list=[]
for i in list:
    if i not in new_list:
        new_list.append(i)
print(new_list)"""
# find missing number
'''numbers = [1, 2, 3, 5, 6, 7]
new_list = []
missing = []
s = numbers[0]
e = numbers[-1]

for i in range(s, e + 1):

    new_list.append(i)
print(new_list)
for j in new_list:
    if j not in numbers:
        missing.append(j)

print(missing)'''
#count digits:
'''n=int(input("enter the number"))
n=abs(n)
count=0
if n==0:
    count=1
while n > 0:
    
     count=count+1
     n=n//10
print(count)'''
