import random
def game():
    t = 0
    g = int(input("Total Guesses : "))
    low = int(input("Enter the lower range : "))
    high = int(input("Enter the higher range : "))
    x = random.randint(low, high)
    n = int(input(" Enter an integer between the given range : "))

    while (x != 'n'):
        if(t < (g-1)):
            if n < x:
                print("the number you have guessed is low")
                t = t+1
                n = int(input(" Enter an integer between the given range : "))
        elif (n>x):
            print('the number you have guessed is high')
            t = t+1
            n = int(input(" Enter an integer between the given range : "))
        else:
            print("the number you have guessed is right")
            print("the total number of guesses is ", t+1)
            break
if __name__==("__main__"):
    game()                