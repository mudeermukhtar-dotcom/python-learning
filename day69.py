#Write a Python program using nested while loops to print this pattern:1|22|333|4444|55554
'''i=1
while i <= 5:
    j=1
    while j<=i:
        print(i,end="")
        j=j+1
    i=i+1
    print()'''
#write a program to print this pattern :1|12|123|1234:
'''i=1
while i <= 5:
    j=1
    while j <= i:
        print(j, end="")
        j=j+1
    i=i+1
    print()'''
#write a program to print this pattern 12345|1234|123|12|1
'''i=5
while i >= 1:
    j=1
    while j <= i:
        print(j,end="")
        j=j+1
    i=i-1
    print()'''
#write a program to print this pattern 54321|5432|543|54|5
'''i=1
while i <= 5:
    j=5-i+1
    while j>=1:
        print(j,end="")
        j=j-1
    i=i+1
    print()'''
    