bal = 5000

def check_balance():
    print(f"The current balance is: {bal}")

def deposit():
    global bal
    added_amount = int(input("Enter the amount to deposit: "))
    if added_amount > 0:
        bal += int(added_amount)
        print(f"The total balance is: {bal}")
    else:
        print("Invalid input. Please enter a non-negative integer.")

def withdraw():
    global bal
    withdrawn_amount = int(input("Enter the amount to withdraw: "))
    if withdrawn_amount >= 0:
        if withdrawn_amount <= bal:
            bal -= withdrawn_amount
            print(f"The total balance is: {bal}")
        else:
            print("Insufficient funds.")
    else:
        print("Invalid input. Please enter a non-negative integer.")

while True:
    choice = input("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit\nEnter the number of the function to use: ")
    if choice == '1':
        check_balance()
    elif choice == '2':
        deposit()
    elif choice == '3':
        withdraw()
    elif choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a valid option.")
