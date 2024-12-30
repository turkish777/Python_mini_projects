# Todo list app mini!


def menu():
    print('\nTodo List Menu:')
    print('1. View Tasks')
    print('2. Add a Task')
    print('3. Remove a Task')
    print('4. Exit')
    
    
def get_choice():
    while True:
        choices = ('1' , '2' , '3' , '4')
        user_choice = input("Enter u coice (1/2/3/4): ")
        if user_choice not in choices:
            print("Invalid choice! ")
        else:
            return user_choice
           
def add_task(tasks):
    while True:
        task = input("Enter the task: ").strip()
        if len(task) != 0:
            tasks.append(task)
            print("Task Added! ")
            break
        else:
            print("INvalid task! ")
            
def delete_task(tasks):
    view_task(tasks)
    
    while True:
        try:
            task_num = int(input("Enter the task number you want to delete: "))
            if 1 <= task_num <= len(tasks):
                tasks.pop(task_num - 1)
                break
            else:
                print('Invalid number! ')
        except ValueError:
            print("Enter a valid number: ")
            
def view_task(tasks):
    if not tasks:
        print("No task found! ")
        return
    
    for index , task in enumerate(tasks , start=1):
        print(f'{index}. {task}')

def main():
    tasks = []
    
    while True:
        menu()
        choice = get_choice()
        
        if choice == '1':
            view_task(tasks)    
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            delete_task(tasks)
        else:
            print("Goodbye! ")
            break
        
        
if __name__ == '__main__':
    main()
    