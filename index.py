# 2. ATM Simulation with Account Lock 
# Simulate a simple ATM system.


# User has 3 attempts to enter the correct PIN.
# If PIN is correct, show menu (Withdraw, Deposit, Check Balance, Exit).
# If all attempts fail, block the account.
# while loop → PIN attempts
# if-elif-else → correct / incorrect / blocked
# Nested while → menu system
# Nested if → balance validation


print("Welcome to the ATM Simulation!")

correct_pin = "1234"
attempts = 3
balance = 1000
while attempts > 0:
    user_pin = input("Please enter your PIN:")
    if user_pin == correct_pin:
        print("PIN is correct. Welcome to the ATM.")
        while True:
            print("\nMenu:")
            print("1. Withdraw")
            print("2. Deposit")
            print("3. Check Balance")
            print("4. Exit")
            choice = input("Please select an option (1-4):")
            if choice == "1":
                amount = float(input("Enter amount to withdraw:"))
                if amount >balance:
                    print("Insufficient balance.")
                else:
                    balance -= amount
                    print(f"You have withdrawn ${amount}. Your new balance is ${balance}.")
            elif choice == "2":
                amount = float(input("Enter amount to deposit:"))
                balance += amount
                print(f"You have deposited ${amount}. Your new balance is ${balance}.")
            elif choice == "3":
                print(f"Your current balance is ${balance}.")
            elif choice == "4":
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")
        break
    else:
        attempts -= 1
        print(f"Incorrect PIN. You have {attempts} attempts left.")
        if attempts == 0:
            print("Your account has been blocked due to too many incorrect attempts.")
        else:
            print("Please try again.")
else:
    print("Your account is blocked. Please contact the bank for assistance.")
    