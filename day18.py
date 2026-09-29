# write a program to find second largest in general:
"""list = [-1, -2, -1, -4, -5]
largest = float("-inf")
second_largest = float("-inf")
for i in list:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i < largest:
        second_largest = i
print(largest, second_largest)
# find the second smallest number in general:
list = [-1, -2, -3, -4, -5, -2]
smallest = float("inf")
second_smallest = float("inf")
for i in list:
    if i < smallest:
        second_smallest = smallest
        smallest = i
    elif i > smallest and i < second_smallest:
        second_smallest = i
print(second_smallest)"""

# find  the third lafgest number:
list = [-1, -2, -5, -6]
largest = float("-inf")
second_largest = float("-inf")
third_largest = float("-inf")
for i in list:
    if i > largest:
        third_largest = second_largest
        second_largest = largest
        largest = i
    elif i > second_largest and i < largest:
        third_largest = second_largest
        second_largest = i
    elif i > third_largest and i < second_largest:
        third_largest = i
print(largest)
print(second_largest)
print(third_largest)
