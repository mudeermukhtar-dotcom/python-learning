#Write a Python program to create a list of 5 numbers and print the first number and the last number.
'''list=[1,2,3,4,5]
print(list[0])
print(list[4])'''
#Write a Python program to create a list of 5 numbers and print the last number using negative indexing.
'''list=[1,2,3,4,5]
print(list[-1])'''
#Write a Python program to create a list of 6 numbers and print the first 3 numbers using slicing.
'''list=[1,2,3,4,5,6]
print(list[0:3])'''
#Create a list of 5 numbers and print the last 3 numbers using slicing
'''list=[1,2,3,4,5,6]
print(list[-3:])'''
#Write a Python program to create a list of 5 numbers and change the 3rd number to 100.
'''list=[1,2,3,4,5,6]
list[2]=100
print(list)'''
#Create a list of 7 numbers and print the elements from index 2 to index 5
'''list=[1,2,3,4,5,6,7]
print(list[2:5])'''
#Create a list of 6 numbers and print the last 3 numbers in reverse order using slicing.
'''list=[1,2,3,4,5,6]
print(list[-1:-4:-1])'''
#Create a list of 5 numbers and use a for loop to print each element.
'''list=[1,2,3,4,5]
for i in list:
    print(i)'''
#Create a list of 6 numbers and use a for loop to print only the even numbers.
'''list=[1,2,3,4,5,6]
for i in list:
    if i%2==0:
        print(i)'''
#Create a list of 6 numbers and use a for loop to print only the odd numbers.
'''list=[1,2,3,4,5,6]
for i in list:
    if i%2 !=0:
        print(i)'''
#create a list of 5 numbers and calculate the sum of all elements using a for loop.
'''list=[10,20,30,40,50]
sum=0
for i in list:
    sum=sum+i
print(sum)'''
#Create a list of numbers and count how many even numbers are present using a for loop
'''list=[1,2,3,4,5,6,7,8]
count=0
for i in list:
    if i %2==0:
        count=count+1
print(count)'''
#Create a list of numbers and find the largest number using a for loop.
'''list=[1,2,3,4,5,6]
largest=list[0]
for i in list:
    if i > largest:
      largest=i
print(largest)'''
##Create a list of numbers and find the smallest number using a for loop:
'''list=[1,2,3,4,5,6]
smallest=list[0]
for i in list:
    if i < smallest:
        smallest=i
print(smallest)'''
#Create a list of 4 numbers and add 5 at the end:
'''list=[10,20,30,40,50]
list.append(60)
print(list)'''
#create a list [10, 20, 30, 40] and add 100 at index 1 :
'''list=[10, 20, 30, 40]
list.insert(1,100)
print(list)'''
#Create a list [10, 20, 30, 40, 50] and remove 30:
'''list=[10, 20, 30, 40,50]
list.remove(30)
print(list)'''
#Create a list [10, 20, 30, 40, 50] and remove the item at index 2 using pop:
'''list=[10, 20, 30, 40, 50] 
list.pop(2)
print(list)'''
#Create a list [7, 2, 9, 1, 5] and sort it in ascending order using
'''list=[7, 2, 9, 1, 5]
list.sort()
print(list)'''
#Create a list [4, 8, 1, 6, 3] and sort it in descending order:
'''list=[4, 8, 1, 6, 3]
list.sort(reverse=True)
print(list)'''
#Create a list [10, 20, 30, 40, 50] and reverse it using reverse().
'''list=[10, 20, 30, 40, 50]
list.reverse()
print(list)'''
#[5, 10, 15, 20, 25] mein 20 ka index index() se find karo?
'''list=[5, 10, 15, 20, 25]
x=list.index(10)
print(x)'''
#Create a list [1, 2, 3, 2, 4, 2, 5] and use count():
'''list=[1, 2, 3, 2, 4, 2, 5]
x=list.count(2)
print(x)'''
