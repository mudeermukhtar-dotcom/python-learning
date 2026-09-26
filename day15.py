#Create a new list containing only the elements of items that are present in numbers.
'''numbers = {10, 15, 20, 25, 30, 35}
items = [10, 12, 20, 22, 35, 50]
result=list(numbers.intersection(items))
print(result)'''
#Create a new list containing only elements from items that are not in numbers.
'''numbers = {10, 20, 30, 40, 50}
items = [10, 15, 20, 25, 30, 60]
result=[]
for i in items:
    if i not in numbers:
        result.append(i)
print(result)'''
#present and missing:
'''numbers = {10, 20, 30, 40, 50}
items = [10, 15, 20, 25, 30, 40]
present=[]
missing=[]
for  i in items:
    if i in numbers:
        present.append(i)
    if i not in numbers:
        missing.append(i)
print("present :", present)
print("missing :",missing)'''
#Remove duplicate elements from a list using a set.
'''items = [10, 20, 10, 30, 20, 40, 30]
x=list(set(items))
print(x)'''
#Find common elements in two lists using a set. output--[30, 40, 50]
'''list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]
x=set(list1)
y=set(list2)
result=[]
for  i in x:
    if i in y:
        result.append(i)

print(list(result))'''
#Find elements that are only in the first list using set. output----[10, 20, 50]
'''list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 60, 70]
x=set(list1)
y=set(list2)
result=[]
for  i in x:
    if i not  in y:
        result.append(i)
print(list(result))'''
#Find elements common to both lists, without duplicates.  outout----[20, 30]
'''list1 = [10, 20, 20, 30, 40, 50]
list2 = [20, 30, 30, 60, 70]
x=set(list1)
y=set(list2)
print(list(x.intersection(y)))'''
#Find the unique elements that appear in only one of the two lists. output---[10, 20, 50, 60, 70]
'''list1 = [10, 20, 20, 30, 40, 50]
list2 = [30, 40, 60, 70, 70]
x=set(list1)
y=set(list2)
result=x.symmetric_difference(y)
print(list(result))'''
#Find the elements that appear in both lists AND are even numbers. output--[20, 30, 40]
'''list1 = [10, 15, 20, 25, 30, 40]
list2 = [20, 30, 35, 40, 50]
x=set(list1)
y=set(list2)
result=list(x.intersection(y))
newresult=[]
for i in result:
    if i %  2 ==0:
        newresult.append(i)
 
print(newresult)'''
#Find the elements that are present in the first list but NOT in the second list,
#and keep only odd numbers. output-----[15, 35, 45]
'''list1 = [10, 15, 20, 25, 30, 35, 40, 45]
list2 = [20, 25, 30, 50]
x=set(list1)
y=set(list2)
result=list(x.difference(y))
newlist=[]
for i in result:
    if i % 2 !=0:
        newlist.append(i)
print(newlist)
'''
#Find the elements that are common in both lists, but appear only once in each list.
#output---[20, 30, 40]
'''list1 = [10, 20, 20, 30, 40, 40, 50]
list2 = [20, 30, 30, 40, 60, 60]
x=set(list1)
y=set(list2)
result=list(x.intersection(y))
newlist=[]
for i in result :
    if list1.count(i)==1 and list2.count(i)==1:
        newlist.append(i)
print(newlist)'''