import random

random_number = random.randint(1, 100)
while True:
    try:
        guess = int(input("Enter the number between 1 & 100: "))
        if guess < random_number:
            print("Number is to Low! ")
        elif guess > random_number:
            print("Number is To High! ")
        else:
            print("You guessed it! Congratulations ")
    except ValueError:
        print("please Enter a valid number! ")
        