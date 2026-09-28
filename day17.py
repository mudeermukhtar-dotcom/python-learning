# find the difference between the largest even number and the smallest odd number.
"""numbers = [12, 5, 18, 7, 20, 9, 14, 3]
big=0
small=9
for i in numbers:
    if i % 2 == 0 and i > big :
        big = i
print("Largest even number :" ,big)
for j in numbers:
    if j % 2 != 0 and j < small :
        small = j
print("SMALLEST ODD NUMBER : ",small)
print("THE DIFFRENCE BETWEEN LARGEST EVEN AND SMALLEST ODD ",big - small)"""

# Question: Find the sum of all even numbers greater than 10.
"""numbers = [12, 7, 18, 5, 20, 9, 14, 3, 25, 30]
Even_list = []
sum=0
for i in numbers :
    if i % 2 == 0 and i > 10:
     Even_list.append(i)
print( Even_list )
for j in Even_list :
     sum = sum + j
print( sum )"""
# Question: Find all numbers that appear exactly once AND are even.
"""numbers = [10, 15, 20, 15, 30, 10, 40, 25, 20, 50]
newlist = []
for i in numbers:
    if i % 2 == 0  and numbers.count(i)==1:
        newlist.append(i)
print(newlist)
"""
# Find the largest odd number and smallest even number, then print their difference.
"""numbers = [12, 5, 18, 7, 20, 9, 14, 3, 25]
l_odd = 0
s_even = None
for i in numbers:
    if i % 2 != 0 and i > l_odd:
        l_odd = i
    if i % 2 == 0:
        if s_even is None or i < s_even:
            s_even = i
diffrence = l_odd - s_even
print(diffrence)"""
# Question: Find all numbers that appear more than once AND are odd
"""numbers = [8, 15, 4, 21, 10, 15, 6, 21, 30]
newlist = []
for i in numbers:
    if i % 2 != 0 and numbers.count(i) > 1:
        newlist.append(i)
print(newlist)"""
# Question: Find the sum of numbers that appear exactly once.
"""numbers = [12, 7, 18, 5, 20, 7, 14, 3, 18, 25]
total = 0
newlist = []
for i in numbers:
    if numbers.count(i) == 1:
        newlist.append(i)
for j in newlist:
    total = j + total
print(total)"""
# Question: Find the largest number that appears exactly once.
"""numbers = [10, 15, 22, 7, 30, 15, 18, 7, 40, 25]
newlist = []
largest = 0
for i in numbers:
    if numbers.count(i) == 1:
        newlist.append(i)
print(newlist)
for j in newlist:
    if j > largest:
        largest = j
print(largest)"""
# Question: Find the second smallest number
'''numbers = [12, 5, 18, 7, 20, 9, 14, 3]
smallest = None
second_smallest = 0
for i in numbers:
    if smallest is None or i < smallest:
        second_smallest = smallest
        smallest = i
    elif i > smallest and i < second_smallest:
        second_smallest = i
print(second_smallest)
'''