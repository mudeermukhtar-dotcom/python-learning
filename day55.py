### Question 1: Create and Add Elements

'''Create a set containing the numbers `{10, 20, 30, 40}`.

1. Print the set.
2. Add `50` to the set.
3. Add `20` again.
4. Print the final set.
5. Print the total number of unique elements using `len()`.

**Rule:** Use the `add()` method.
#sol:
numbers={10,20,30,40,}
print(numbers)
numbers.add(50) #adds 50 
print(numbers)
numbers.add(20)  #not add 20 beacuse 20 is already there
print(numbers)
print(len(numbers))'''
###question 2:Remove Duplicates from a List
'''You are given the following list:

python
numbers = [10, 20, 10, 30, 20, 40, 50, 30]
Write a Python program to:

1. Convert the list into a set.
2. Print the set.
3. Convert the set back into a list.
4. Print the final list.
5. Print the number of unique elements.

**Rules:** Use `set()`, `list()`, and `len()
#sol
numbers = [10, 20, 10, 30, 20, 40, 50, 30]
new_numbers=set(numbers)
print(new_numbers)
old_numbers=list(new_numbers)
print(old_numbers)
print(len(new_numbers))'''
#— Find Common Elements
'''Two groups of students play different games:


cricket = {"Ali", "Mudeer", "Rahul", "Zoya"}
football = {"Mudeer", "Zoya", "Ayaan", "Sameer"}


Write a Python program to:

1. Find the students who play **both cricket and football**.
2. Print the result.
3. Count how many students play both games.

**Rule:** Use the set intersection operator `&`.
#sol
cricket = {"Ali", "Mudeer", "Rahul", "Zoya"}
football = {"Mudeer", "Zoya", "Ayaan", "Sameer"}
all_rounder=cricket&football   #add ist and 2nd and removes coomon
print(all_rounder)
print(len(all_rounder))   #prints how many students play both games'''
#
### Question 1: Student Club Analyzer

'''```python
coding = {"Ali", "Mudeer", "Rahul", "Zoya", "Ayaan"}
gaming = {"Mudeer", "Zoya", "Sameer", "Kabir"}
music = {"Ali", "Zoya", "Sameer", "Ayaan"}
```

Write a Python program to:

1. Find students who enjoy both coding and gaming.
2. Find students who enjoy coding but not music.
3. Find students who enjoy exactly one activity.
4. Find students who enjoy all three activities.
5. Count the total number of unique students.

**Rules:**
- Use set operations: `&`, `|`, `-`, `^`.
- Don't use loops.
- Store each result in a separate variable.
'''
coding = {"Ali", "Mudeer", "Rahul", "Zoya", "Ayaan"}
gaming = {"Mudeer", "Zoya", "Sameer", "Kabir"}
music = {"Ali", "Zoya", "Sameer", "Ayaan"}
candg=coding&gaming
coding=coding-music
onlyone=coding^gaming
print(onlyone)