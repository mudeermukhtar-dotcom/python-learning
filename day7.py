#Write a Python program to find the number of elements in a list :
'''list= [12, 45, 23, 67, 89, 10]
print(len(list))'''
#Write a Python program to find the smallest number in a list:
'''numbers=[45, 12, 67, 23, 89, 10]
print(min(numbers))'''
#Write a Python program to find the largest number in a list :
'''list=[45, 12, 67, 23, 89, 10]
print(max(list))'''
#Write a Python program to find the sum of all numbers in a list using sum().
'''list=[45, 12, 67, 23, 89, 10]
print(sum(list))'''
#Write a Python function that takes a list as an argument and prints the largest number :
'''numbers=[1,2,3,4,5,6,7]

def largest(numbers):
 print(max(numbers))
largest(numbers)'''
#Write a Python function that takes a list as an argument and prints the smallest number:
'''numbers=[1,2,3,4,5,6,7]
def smallest(numbers):
    print(min(numbers))
smallest(numbers)'''
#write a Python function that takes a list as an argument and prints the sum of all numbers.
'''numbers=[1,2,3,4,5,6,7,8]
def add(numbers):
    print(sum(numbers))
add(numbers)'''
#Write a Python function that takes a list as an argument and prints the number of even numbers in the list:
'''numbers=[1,2,3,4,5,6,3,4,5,6]
def check_even(numbers):
    count=0
    for i in numbers:
     if i%2==0:
        count=count+1
    print(count)
check_even(numbers)'''
#Write a Python function that takes a list as an argument and prints the number of odd numbers in the list.
'''numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def count_odd(numbers):
    count=0
    for i in numbers:
        if i%2!=0:
            count=count+1
    print(count)
count_odd(numbers)'''
#Write a Python function that takes a list as an argument and prints the average of all numbers in the list.
'''numbers = [10, 20, 30, 40, 50]
def find_average(numbers):
    average=sum(numbers)/len(numbers)
    print(average)
find_average(numbers)'''
#Write a Python function that takes a list as an argument and adds 100 to the end of the list using append().
# Then print the updated list:
'''numbers = [10, 20, 30, 40]
def add_number(numbers):
    numbers.append(100)
    print(numbers)
add_number(numbers)'''
#Write a Python function that takes a list as an argument and removes the last element using pop(),
#  then prints the updated list.
'''numbers = [10, 20, 30, 40, 50]
def remove(numbers):
    numbers.pop(-1)
    print(numbers)
remove(numbers)'''
#write a Python function that takes a list as an argument and removes the first occurrence of 20 using remove(),
#  then prints the updated list.
'''numbers = [10, 20, 30, 20, 40]
def remove_numbers(numbers):
    numbers.remove(20)
    print(numbers)
remove_numbers(numbers)'''
#Write a Python function that takes a list as an argument and sorts the list in ascending order using sort(), 
# then prints the list
'''numbers = [50, 10, 40, 20, 30]
def ascending(numbers):
    numbers.sort()
    print(numbers)
ascending(numbers)'''
#Write a Python function that takes a list as an argument and sorts the list in descending order using sort(reverse=True), 
#then prints the list.
'''numbers = [10, 50, 20, 40, 30]
def desending(numbers):
    numbers.sort(reverse=True)
    print(numbers)
desending(numbers)'''
#Write a Python function that takes a list as an argument and reverses the list using reverse(), then prints the updated list.
''''ers = [10, 20, 30, 40, 50]
def revese_number(numbers):
    numbers.reverse()
    print(numbers)
revese_number(numbers)'''