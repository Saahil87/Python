from random import randint

rand_num = randint(0,2)

print("Rock...")
print("Paper...")
print("Scissors...")

player1 = input("Player1 make your move: ")

if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"
else:
    computer = "scissors"

print(f"Computer plays {computer}")

if player1 == computer:
    print("It's a tie!")
elif player1 == "rock":
    if computer == "scissors":
        print("Player1 wins!")
    elif computer == "paper":
        print("computer wins!")
elif player1 == "paper":
    if computer == "rock":
        print("Player1 wins!")
    elif computer == "scissors":
        print("computer wins!")
elif player1 == "scissors":
    if computer == "paper":
        print("Player1 wins!")
    elif computer == "rock":
        print("computer wins!")
else:
    print("Something went wrong!")
