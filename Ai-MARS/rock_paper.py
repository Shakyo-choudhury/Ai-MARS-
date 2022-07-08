import random
def game():
    user = int(input("enter any of the follwing options: (1)Rock, (2)Paper, (3)Scissor: "))
    computer = random.randint(1,3)
    score = 0
    if computer == user:
        score = score
        print(f"draw match!{score}")
    elif computer == 1 and user == 2:
        score = score + 1
        print(f"you won and the score is: {score}")
    elif computer == 2 and user == 1:
        score = score
        print("computer has won!")
    elif computer == 2 and user == 3:
        score = score + 1
        print(f"you have won and the score is {score}")
    elif computer == 3 and user == 2:
        score = score
        print(f"computer has won!")
    elif computer == 1 and user == 3:
        score = score 
        print("computer has won!")
    elif computer == 3 and user  == 1:
        score = 1 + score
        print(f"you have won and the score is {score}")
    else:
        print("invalid input")
while True:
    game()