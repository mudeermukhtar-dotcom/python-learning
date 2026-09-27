#Q1)Find all unique even numbers and store them in a new list.
#EXPECTED OUTPUT -----[10, 20, 30, 40, 50]
'''numbers = [10, 15, 20, 15, 30, 40, 20, 50, 35]
even=[]
for i in numbers:
    if i % 2 == 0:
        even.append(i)
newnumbers=set(even)
print(list(newnumbers))'''
#Q2)Count how many numbers in the tuple are:
#1.even
#2.odd
#3.greater than 30
'''numbers = (10, 15, 20, 25, 30, 35, 40, 45, 50)
count_even = 0
count_odd=0
count_greater=0
for i in numbers :
    if i % 2 == 0:
        count_even += 1
    if i % 2 != 0:
        count_odd += 1
    if i > 30:
        count_greater +=1
print("EVEN :",count_even)
print("ODD :",count_odd)
print("GREATER THAN 30 :",count_greater)'''
#Find the numbers that appear more than once in the list.
'''numbers = [10, 20, 15, 20, 30, 15, 40, 50, 10]
newlist=[]
for i in numbers:
    if numbers.count(i) > 1:
        newlist.append(i)
print(list(set(newlist)))'''
#Find the largest odd number in the list without using max().
'''numbers = [10, 15, 20, 25, 30, 35, 40, 45, 50]
new_list=[]
big=0
for i in numbers:
    if i  % 2 != 0:
        new_list.append(i)
for i in new_list:
    if i > big:
        big  = i
print("the largest odd number in the list is ",big)'''
#Find all elements that are present in either list but NOT in both lists.
'''list1 = [10, 20, 30, 40, 50]
list2 = [20, 40, 60, 80]
new_list1=set(list1)
new_list2=set(list2)
result=new_list1.symmetric_difference(new_list2)
print(list(result))'''
#Find the number that appears the most times in the list.
'''numbers = [10, 15, 20, 15, 30, 20, 40, 15, 50]

big=0
coomon=0
for i in numbers:
    x=numbers.count(i)
    
    if x > big:
        big = x
        common=i
print(common)'''
#Find all numbers that appear exactly once in the list:
'''numbers = [10, 15, 20, 10, 25, 30, 15, 40, 20, 50]
newlist=[]
for  i in numbers:
    if numbers.count(i)==1:
        newlist.append(i)
print(newlist)'''
#Find the second largest number without using max() or sort().
'''numbers = [12, 7, 18, 5, 20, 9, 14, 3]
big = 0
big2=0
newlist=[]
for i in numbers :
    if i > big :
        big = i
numbers.remove(big)
print(numbers)
for j in numbers:
    if j > big2:
        big2 = j
print("te second largest number is"big2)'''
'''numbers = [12, 7, 18, 5, 20, 9, 14, 3]
largest=0
second_largest=0
for i in numbers:
    if i > largest:
        second_largest=largest
        largest =i
    elif i > second_largest:
        second_largest=i
print(second_largest)'''
#Find the numbers that appear exactly once AND are greater than 20
numbers = [10, 15, 20, 10, 25, 30, 15, 40, 20, 50]
newlistg=[]
newlistc=[]
for i in numbers:
    if numbers.count(i)==1 and i > 20:
        newlistc.append(i)
   
print(newlistc)










    


