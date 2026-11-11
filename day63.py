# Q4. Find the second-highest distinct marks and print
# the name of the student who achieved them.

'''students = {
    "Ali": 78,
    "Rahul": 92,
    "Aman": 65,
    "Zoya": 88,
    "Sara": 85
}

highest = 0
second_highest = 0
highest_name = ""
second_highest_name = ""

for key, value in students.items():
    if value > highest:
        second_highest = highest
        second_highest_name = highest_name
        highest = value
        highest_name = key

    elif value > second_highest and value < highest:
        second_highest = value
        second_highest_name = key

print(
    f"{second_highest_name} is the second topper "
    f"of the class and has scored {second_highest}"
)
'''

# Q5. Create a new dictionary to count the number of
# pass and fail students. A score of 50 or above is a pass.

'''students = {
    "Ali": 78,
    "Rahul": 92,
    "Aman": 35,
    "Zoya": 88,
    "Sara": 42,
    "Usman": 29,
    "Riya": 65
}'''