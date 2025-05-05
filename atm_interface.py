class BankAccount:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of ₹{amount} successful. Remaining balance: ₹{self.balance:.2f}")
            return True
        elif amount <= 0:
            print("Invalid withdrawal amount. Please enter a positive value.")
            return False
        else:
            print("Insufficient balance for withdrawal.")
            return False

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of ₹{amount} successful. New balance: ₹{self.balance:.2f}")
            return True
        else:
            print("Invalid deposit amount. Please enter a positive value.")
            return False

    def check_balance(self):
        print(f"Your current balance is: ₹{self.balance:.2f}")

    def verify_pin(self, entered_pin):
        return self.pin == entered_pin

class ATM:
    def __init__(self, account):
        self.account = account

    def display_menu(self):
        print("\n--- ATM Menu ---")
        print("1. Withdraw")
        print("2. Deposit")
        print("3. Check Balance")
        print("4. Exit")

    def run(self):
        print("Welcome to the ATM!")
        attempts = 3
        while attempts > 0:
            pin = input("Enter your PIN: ")
            if self.account.verify_pin(pin):
                print("PIN verified successfully.")
                break
            else:
                attempts -= 1
                print(f"Incorrect PIN. You have {attempts} attempts remaining.")
        else:
            print("Too many incorrect PIN attempts. Account locked.")
            return

        while True:
            self.display_menu()
            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                amount_str = input("Enter the amount to withdraw: ₹")
                try:
                    amount = float(amount_str)
                    if amount > 0:
                        self.account.withdraw(amount)
                    else:
                        print("Invalid amount. Please enter a positive value.")
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")

            elif choice == '2':
                amount_str = input("Enter the amount to deposit: ₹")
                try:
                    amount = float(amount_str)
                    if amount > 0:
                        self.account.deposit(amount)
                    else:
                        print("Invalid amount. Please enter a positive value.")
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")

            elif choice == '3':
                self.account.check_balance()

            elif choice == '4':
                print("Thank you for using the ATM!")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    # Create a sample bank account
    user_account = BankAccount("123456", "1234", 1000)

    # Create an ATM instance connected to the user's account
    atm = ATM(user_account)

    # Run the ATM interface
    atm.run()
