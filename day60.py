#functions example 
'''def total(a,b,c):
    total=a+b+c
    return total
print(total(10,20,30))'''
#example 2
'''def maximum(a,b,c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c
print(maximum(10,20,30))'''
#example 3
'''def maximum(*args):
    largest=args[0]
    for num in args:
        if num > largest:
            largest=num
    return largest
print(maximum(10, 50, 30, 90, 20))'''
#example 4
'''def greet(**krawgs):
    print(krawgs)
greet(name="mudeer",age=18)'''
#recursion
def number(i, n):
    if i > n:
        return

    print(i)
    number(i + 1, n)

number(1, 10)
