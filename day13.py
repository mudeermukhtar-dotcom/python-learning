#Write a Python function using recursion to print even numbers from n down to 2.
'''def evendown(n):
    if n == 0:
        return
    print(n)
    evendown(n-2)
evendown(10)'''
#Write a Python function using recursion to print odd numbers from n down to 1.
'''def odddown(n):
    if n == 0:
     return
    if n % 2!= 0:
     print(n)
    odddown(n-1)
   
odddown(10)'''
#Write a Python function using recursion to calculate the factorial of a number.
'''def factorial(n):
    if n == 0 or n == 1:
        return 1
    return (n*factorial(n-1))
print(factorial(5))'''
#rite a Python function using recursion to find the sum of all even numbers from 1 to n.
'''def sumeven(n):
    if n ==0 :
        return 0
    
    return n + sumeven(n-2)

print(sumeven(6))'''
#Write a Python function using recursion to find the sum of all odd numbers from 1
'''def oddsum(n):
    if n == 0 :
        return 0
    if n % 2 != 0:
        return n + oddsum(n-1)
    else:
        return oddsum(n-1)
print(oddsum(5))'''
#Write a Python function using recursion to count how many even numbers are present from 1 to n.

'''def counteven(n):
    if n==0:
        return 0
    if n % 2== 0:
        return 1 + counteven(n-1)
    else:
        return counteven(n-1)
print(counteven(6))'''
#Write a Python function using recursion to count how many odd numbers are present from 1 to n.
'''def oddsum(n):
    if n == 0:
        return 0
    if n % 2 != 0:
        return 1 + oddsum(n-1)
    else:
        return oddsum(n-1)
print(oddsum(10))'''

#Write a Python function using recursion to find the largest digit in a number.
'''def largest(n , big=0):
    if n ==0  :
        return big 
    digit = n % 10
    if digit > big:
        big = digit
    return largest(n//10,big)
print(largest(391))'''
#Write a Python function using recursion to find the smallest digit in a number.
'''def smallest(n,small=9):
    if n==0 :
        return small
    digit= n%10
    if digit < small :
        small=digit
    return smallest(n//10,small)
print(smallest(123)) '''
#Write a Python function using recursion to count the number of digits in a number.
'''def count_digits(n,initial=0):
    if n == 0:
        return initial
    digit=n%10
    
    initial=initial+1
    return count_digits(n//10,initial)
print(count_digits(1234510))'''
#Write a Python function using recursion to find the sum of all digits of a number.
'''def sum_digit(n,total=0):
    if n ==0:
        return total
    digit=n%10
    total += digit
    return sum_digit(n//10,total)
print(sum_digit(1011))'''
##Write a Python function using recursion to find the sum of all digits of a number.
'''def count_even(n,initial=0):
    if n == 0:
        return initial
    digit=n%10
    if digit % 2 == 0:
      initial += 1
      return  count_even(n//10,initial)
    else:
       return count_even(n//10,initial)
print(count_even(123))'''
#Write a Python function using recursion to count how many odd digits are present in a given number.
'''def odd_count(n, initial=0):
    if n ==0:
        return initial
    digit = n % 10
    if digit % 2 != 0:
        initial += 1
        return odd_count(n//10,initial)
    else:
       return odd_count(n//10,initial)
print(odd_count(123))'''

