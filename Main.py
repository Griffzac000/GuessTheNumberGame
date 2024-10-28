import random

random_num = random.randint(1, 10)

while True:
    guess = int(input("Enter your guess: "))

    if guess > random_num:
        print("Too high!, Try again.")
    elif guess < random_num:
        print("Too low!, Try again.")
    else:
        print("Print Congratulations! You've guessed the number.")
        break
