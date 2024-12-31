# # Atm machine --------

class ATM:
    def __init__(self):
        self.balance = 0
        
    def check_balance(self):
        return self.balance
    
    def deposit(self , amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")

        
        self.balance += amount
        
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError(f"Insufficient funds. Your balance is: ${self.balance:.2f}")
        self.balance -= amount
            
        
class AtmContoller:
    def __init__(self):
            self.atm = ATM()
            
            
    def get_number(self , prompt):
        while True:
            try:
                value = float(input(prompt))
                return value
            except ValueError:
                print("Invalid input . Please enter a number .")
                
            
    def display_menu(self):
        print("\n Welcome to the ATM machine")
        print('*'*20)
        print("1. Add money")
        print("2. See money")
        print("3. Withdraw money")
        print("4. Exit")
        
        
    def check_balance(self):
        balance = self.atm.check_balance()
        print(f"Your current balance is: ${balance:.2f}")

        
    def deposit(self):
        while True:
            try:
                amount = self.get_number("Enter the amount to deposit: ")
                self.atm.deposit(amount)
                print(f"Amount deposited: ${amount:.2f}.")
                break
            except ValueError as errro:
                print(errro)
                
    def withdraw(self):
        try:
            amount = self.get_number("Enter the amount to withdraw: ")
            self.atm.withdraw(amount)
            print(f"Amount withdrawn: ${amount:.2f}")
        except ValueError as error:
            print(error)
        
                   
    def run(self):
        while True:
            self.display_menu()
                
            choice = input("Please choice and option: ")
            if choice == "1":
                self.deposit()
            elif choice == "2":
                self.check_balance()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
                    
                        
def main():
    atm = AtmContoller()
    atm.run()
            
if __name__ == "__main__":
    main()
                
