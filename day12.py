import random

user = input("Choose rock, paper or scissors: ")

computer = random.choice(["rock", "paper", "scissors"])

print("Computer chose:", computer)

if user=="rock"and computer=="scissors":
     print("user wins")
elif user=="rock"  and computer=="paper":
     print("computer wins")
elif user=="rock" and computer=="rock":
     print("match draw")
elif user=="paper" and computer=="paper":
     print("match draws")
elif user=="paper" and computer=="scissors":
     print("computer wins")
elif user=="paper" and computer=="rock":
     print("user wins",)
elif user=="scissors" and computer=="paper":
     print("user wins")
elif user=="scissors" and computer=="rock":
     print("computer wins")
elif user=="scissors" and computer=="scissors":
     print("match draws")
else:
     print("wrong input")
