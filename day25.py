print("="*50)
print("WECOLME TO KBC".center(50))
print("="*50)
questions = [
    [
        "Q1. What is the capital of India?",
        "A) Mumbai",
        "B) New Delhi",
        "C) Kolkata",
        "D) Chennai",
        "B",
    ],
    [
        "Q2. How many days are there in a leap year?",
        "A) 364",
        "B) 365",
        "C) 366",
        "D) 367",
        "C",
    ],
    [
        "Q3. Which planet is known as the Red Planet?",
        "A) Venus",
        "B) Mars",
        "C) Jupiter",
        "D) Mercury",
        "B",
    ],
    [
        "Q4. Which is the largest ocean on Earth?",
        "A) Atlantic Ocean",
        "B) Indian Ocean",
        "C) Arctic Ocean",
        "D) Pacific Ocean",
        "D",
    ],
    [
        "Q5. Who wrote the Indian national anthem?",
        "A) Mahatma Gandhi",
        "B) Rabindranath Tagore",
        "C) Subhas Chandra Bose",
        "D) Sarojini Naidu",
        "B",
    ],
    [
        "Q6. What is the chemical symbol for gold?",
        "A) Ag",
        "B) Gd",
        "C) Au",
        "D) Go",
        "C",
    ],
    [
        "Q7. Which is the largest planet in our Solar System?",
        "A) Saturn",
        "B) Earth",
        "C) Jupiter",
        "D) Neptune",
        "C",
    ],
    [
        "Q8. In Python, which keyword is used to define a function?",
        "A) function",
        "B) define",
        "C) def",
        "D) fun",
        "C",
    ],
    [
        "Q9. What is the decimal value of binary 1010?",
        "A) 8",
        "B) 10",
        "C) 12",
        "D) 14",
        "B",
    ],
    [
        "Q10. Which data structure stores key-value pairs in Python?",
        "A) List",
        "B) Tuple",
        "C) Set",
        "D) Dictionary",
        "D",
    ],
]
prizes = [
    "₹1,000",
    "₹2,000",
    "₹3,000",
    "₹5,000",
    "₹10,000",
    "₹20,000",
    "₹40,000",
    "₹80,000",
    "₹1,60,000",
    "₹3,20,000",
]
money = 0
for i in range(0, len(questions)):
    question = questions[i]
    print(f"question for rs {prizes[i]}:")
    print(question[0])
    print(f"{question[1]}       {question[2]}")
    print(f"{question[3]}       {question[4]}")
    user = str(input("enter your answer")).upper()
    if user == question[5]:
        print(f"correct answer!. you wan won rs {prizes[i]}")
        if i == 3:
            money = 5000

        elif i == 7:
            money = 80000

        elif i == 9:
            money = 320000
            print("🎉 Congratulations! You are the KBC Champion!")
            print("You have won ₹3,20,000!")

    else:
        print("❌ Wrong Answer!")
        print("You have lost the game.")
        print("Better luck next time!")

        break
print(f"The total amount you have won {money}")
