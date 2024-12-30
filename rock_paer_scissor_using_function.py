## this game is same as last , but there is code using the function's
import random

emojis = { 'r': 'ROCk', 's': '✂️', 'p': '📃' }
choices = ('r' , 'p' , 's')


def get_user_choice():
    while True:
        user_choice = input("choise , Rock , paper , Scissors (r/p/s): ").lower()
        if user_choice in  choices:
            return user_choice
        else:
            print("invalid choice!")

def display_choice(user_choice , computer_choice):
    print(f"User choice {emojis[user_choice]}")
    print(f"computer choice {emojis[computer_choice]}")
    
    
def determiner_winner(user_choice , computer_choice):
        if user_choice == computer_choice:
            print("Tie!")
        elif(
            (user_choice == 'r' and computer_choice == 's') or
            (user_choice == 's' and computer_choice == 'p') or 
            (user_choice == 'p' and computer_choice == 'r')):
            print("You win! ")
        else:
            print("You loss! ")
            
            
def play_game():
    while True:
        user_choice = get_user_choice()
        computer_choice = random.choice(choices)
        display_choice(user_choice , computer_choice)
        determiner_winner(user_choice , computer_choice)
        
        play_again = input("Wnat to play again (y/n): ").lower()
        if play_again == 'n':
            break
        
        
play_game()
        