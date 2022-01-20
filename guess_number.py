import random
num = random.randint(1, 10)#generating a random number
guess = None#initially guess number is zero


while guess != num:
    #while guess!=number we ask the user to enter the number
    guess = input("guess a number between 1 and 10: ")
    guess = int(guess)

    if guess == num:
        print("congratulations! you won!")
        break
    elif guess < num:
        print("Higher number please!")
    elif guess > num:
        print("Lower number please!")
