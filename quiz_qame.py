import random
from termcolor import cprint


QUESTION = 'question'
OPTIONS = 'options'
ANSWER = 'answer'


def ask_question(index , question, options):
    print(f'Question {index}: {question}')
    for option in options:
        print(option)
        
    return input("your Answer: ").upper().strip()


def run_quiz(quiz):
    random.shuffle(quiz)
    
    score = 0 
    for index , item in enumerate(quiz , 1):
        answer = ask_question(index , item[QUESTION] , item[OPTIONS])
        
        if answer == item[ANSWER]:
            cprint('Correct!' , 'green')
            score += 1
        else:
            cprint(f'Wrong! the correct option is {item[ANSWER]}' , 'red')
            
        print()
       
    print(f'Quiz over! U final score is {score} out of {len(quiz)}') 
    
def main():
    quiz = [
        {
            QUESTION: "what is capital of pakistan: ",
            OPTIONS: ["A. Islamabad" , "B. Karachi" , "C. Queta" , "D. Punjab"],
            ANSWER: 'A'
        },
        {
            QUESTION: "What is the national language of Pakistan?",
            OPTIONS: ["A. Pujabi", "B. English", "C. Urdu", "D. Sindhi"],
            ANSWER: 'C'
        },
        {
            QUESTION: "Who is the founder of Pakistan?",
            OPTIONS: ["A. Allama Iqbal", "B. Liaquat Ali Khan", "C. Muhammad Ali Jinnah", "D. Sir Syed Ahmed Khan"],
            ANSWER: 'C'
        },
        {
            QUESTION: "What is the national animal of Pakistan?",
            OPTIONS: ["A. Elphemant", "B. Tiger", "C. Lion", "D. Markhor"],
            ANSWER: 'D'
        },
        {
            QUESTION: "What is the highest mountain in Pakistan?",
            OPTIONS: ["A. K2", "B. Nanga Parbat", "C. Broad Peak", "D. Tirich Mir"],
            ANSWER: 'A'
        },
        {
            QUESTION: "Which city is known as the 'City of Lights' in Pakistan?",
            OPTIONS: ["A. Lahore", "B. Karachi", "C. Islamabad", "D. Peshawar"],
            ANSWER: 'B'
        }
    ]
    run_quiz(quiz)
    
if __name__ == "__main__":
    main()
    



