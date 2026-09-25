#Write a Python function using recursion to find the difference between the largest digit and the smallest digit of a number.
'''def diffrence(n,small=9,big=0):
    if n == 0 :
        return big - small
    digits=n%10
    digitb=n%10
    if digits < small:
      small= digits
    if digitb > big:
      big = digitb
    return diffrence(n//10,small,big)
  
print(diffrence(2349))'''
#Write a Python function using recursion to check whether a number is a palindrome.
# Write a Python function using recursion to check whether a number is a palindrome.

'''def palindrome(n, reverse=0, original=None):

    if original is None:
        original = n

    if n == 0:
        if reverse == original:
            return "It is a palindrome"
        else:
            return "It is not a palindrome"

    reverse = (reverse * 10) + n % 10

    return palindrome(n // 10, reverse, original)


print(palindrome(121))'''
#Write a Python program to create a set containing the numbers 10, 20, 30, 40, and 50.
#  Print the set and also print the total number of elements present in the set.
'''set = { 10 , 20 , 30 , 40 , 50}
print(set)
print(len(set))'''
#Write a Python program to create a set containing the numbers 10, 20, and 30. Add the number 40 to the set using the appropriate set method,
#and then print the updated set.
'''set = { 10 , 20 , 30 }
set.add(4)
print(set)'''
#Write a Python program to create a set containing the numbers 10, 20, 30, and 40. Remove the number 20 from the set using the appropriate set method,
# and then print the updated set.
'''set = { 10 , 20 , 30 , 40 }
set.remove(40)
print(set)'''
#Write a Python program to create a set containing the numbers 10, 20, 30, and 40. Use the discard() method to remove the number 30 from the set, 
# and then print the updated set.
'''set = { 10 , 20 , 30 , 40 }
set.discard(30)
print(set)'''
#Write a Python program to create a set containing the numbers 10, 20, 30, and 40. Use the pop() method
# to remove one element from the set, and then print the updated set.
'''set = { 10 , 20 , 30 , 40}
x=set.pop()
print(set)
print(x)'''
#Write a Python program to create a set containing the numbers 10, 20, 30, and 40. 
# Use the clear() method to remove all elements from the set, and then print the set.
'''set = { 10 , 20 , 30 , 40}
set.clear()
print(set)'''
#Use the union() method to combine both sets and print the resulting set
'''set1 = {10, 20, 30}
set2 = {30, 40, 50}
print(set1.union(set2))'''
#Use the intersection() method to find and print the elements that are common in both sets.
'''set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}
print(set1.intersection(set2))'''
#Use the difference() method to find and.
#print the elements that are present in set1 but not present in set2.
'''set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}
print(set1.difference(set2))'''
#Use the symmetric_difference() method to find and print all the elements 
# that are present in either set1 or set2, but not in both.

'''set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}
print(set1.symmetric_difference(set2))'''
#Elements common to both sets.
#Elements present only in set1.
#Elements present only in set2.
'''set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.union(set2))
print(set1.difference(set2))
print(set2.difference(set1))'''
