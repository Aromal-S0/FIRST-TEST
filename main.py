# main.py

from user import create_user, authenticate_user
from account import deposit, withdraw, get_balance

def main():
    print("Welcome to Simple Bank!")
    
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            if create_user(username, password):
                print("User created successfully!")
            else:
                print("User already exists!")

        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            if authenticate_user(username, password):
                print(f"Welcome, {username}!")
                while True:
                    print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Logout")
                    option = input("Choose an action: ")

                    if option == "1":
                        amt = float(input("Enter amount to deposit: "))
                        if deposit(username, amt):
                            print("Deposit successful.")
                        else:
                            print("Invalid amount.")

                    elif option == "2":
                        amt = float(input("Enter amount to withdraw: "))
                        if withdraw(username, amt):
                            print("Withdrawal successful.")
                        else:
                            print("Insufficient balance or invalid amount.")

                    elif option == "3":
                        print(f"Current balance: ₹{get_balance(username)}")

                    elif option == "4":
                        break
                    else:
                        print("Invalid option.")
            else:
                print("Invalid credentials.")

        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
## simple things