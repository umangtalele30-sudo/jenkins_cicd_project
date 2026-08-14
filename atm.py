import os
import json


# Create accounts.json if it doesn't exist
if not os.path.exists("accounts.json"):
    accounts = {
        "414951": {
            "name": "Umang",
            "balance": 50000,
            "transactions": []
        },
        "9604": {
            "name": "Utkarsha Chopade",
            "balance": 25000,
            "transactions": []
        },
        "4149": {
            "name": "Harshal Chopade",
            "balance": 70000,
            "transactions": []
        }
    }

    with open("accounts.json", "w") as file:
        json.dump(accounts, file, indent=4)

# Load accounts from JSON
with open("accounts.json", "r") as file:
    accounts = json.load(file)

# 3 PIN Attempts
attempt = 0

while attempt < 3:
    entered_pin = input("Enter PIN: ")

    if entered_pin in accounts:
        print("Login Successful")
        break
    else:
        attempt += 1
        print("Incorrect PIN")

if attempt == 3:
    print("Your card has been blocked.")
    exit()

while True:

    print("\nWelcome", accounts[entered_pin]["name"])

    print("\n===== ATM MENU =====")
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Check Balance")
    print("4. Change PIN")
    print("5. Mini Statement")
    print("6. Fast Cash")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        amount = int(input("Enter amount: "))

        if amount <= accounts[entered_pin]["balance"]:

            accounts[entered_pin]["balance"] -= amount
            accounts[entered_pin]["transactions"].append(f"Withdraw ₹{amount}")

            print("Transaction Successful")
            print("Remaining Balance:", accounts[entered_pin]["balance"])

        else:
            print("Insufficient Balance")

    elif choice == 2:

        amount = int(input("Enter Deposit Amount: "))

        accounts[entered_pin]["balance"] += amount
        accounts[entered_pin]["transactions"].append(f"Deposit ₹{amount}")

        print("Deposit Successful")
        print("Current Balance:", accounts[entered_pin]["balance"])

    elif choice == 3:

        print("Current Balance:", accounts[entered_pin]["balance"])

    elif choice == 4:

        new_pin = input("Enter New PIN: ")

        if new_pin not in accounts:

            accounts[new_pin] = accounts.pop(entered_pin)
            entered_pin = new_pin

            print("PIN Changed Successfully")

        else:
            print("PIN already exists.")

    elif choice == 5:

        print("\nMini Statement")

        if len(accounts[entered_pin]["transactions"]) == 0:
            print("No Transactions")

        else:
            for t in accounts[entered_pin]["transactions"]:
                print(t)

    elif choice == 6:

        print("1. ₹500")
        print("2. ₹1000")
        print("3. ₹2000")
        print("4. ₹5000")

        option = int(input("Select option: "))

        if option == 1:
            amount = 500
        elif option == 2:
            amount = 1000
        elif option == 3:
            amount = 2000
        elif option == 4:
            amount = 5000
        else:
            amount = 0

        if amount <= accounts[entered_pin]["balance"]:

            accounts[entered_pin]["balance"] -= amount
            accounts[entered_pin]["transactions"].append(f"Fast Cash ₹{amount}")

            print("Please collect your cash.")
            print("Remaining Balance:", accounts[entered_pin]["balance"])

        else:
            print("Insufficient Balance")

    elif choice == 7:

        # Save all changes before exiting
        with open("accounts.json", "w") as file:
            json.dump(accounts, file, indent=4)

        print("Thank You For Using Our ATM")
        break

    else:
        print("Invalid Choice")