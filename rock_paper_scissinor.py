import random

emojis = { 'r': 'ROCk', 's': '✂️', 'p': '📃' }
choices = ('r' , 'p' , 's')

while True:
    user_choice = input("choise , Rock , paper , Scissors (r/p/s): ").lower()
    if user_choice not in  choices:
        print("Invalid input ")
        continue
        
    computer_choice  = random.choice(choices)
    print(f"User choice {emojis[user_choice]}")
    print(f"computer choice {emojis[computer_choice]}")

    if user_choice == computer_choice:
        print("Tie!")
    elif(
        (user_choice == 'r' and computer_choice == 's') or
        (user_choice == 's' and computer_choice == 'p') or 
        (user_choice == 'p' and computer_choice == 'r')):
        print("You win! ")
    else:
        print("You loss! ")
        
    play_again = input("Want to play again (y/n): ").lower()
    if play_again == 'n':
        break