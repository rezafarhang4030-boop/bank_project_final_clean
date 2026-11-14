from account import BankAccount
from bank import Bank


bank = Bank()


def read_amount(prompt: str) -> float | None:
    """Read a numeric amount from the user; return None if invalid."""
    try:
        amount = float(input(prompt))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return None

    if not BankAccount.is_valid_amount(amount):
        print("Amount must be a finite number greater than zero.")
        return None
    return amount


def create_account() -> None:
    owner = input("Enter account owner's name: ").strip()
    account_number = input("Enter account number: ").strip()

    if not owner or not account_number:
        print("Owner name and account number cannot be empty.")
        return

    existing = bank.find_account_by_number(account_number)
    if existing is not None:
        print("That account number already exists.")
        return

    raw_balance = input("Enter initial balance (press Enter for 0): ").strip()
    if not raw_balance:
        balance = 0
    else:
        try:
            balance = float(raw_balance)
        except ValueError:
            print("Invalid balance. Please enter a number.")
            return

    try:
        account = BankAccount(owner, account_number, balance)
    except ValueError as error:
        print(f"Could not create account: {error}")
        return

    if bank.add_account(account):
        print("Account created successfully.")
    else:
        print("Could not create account. Check the account details.")


def check_balance() -> None:
    account_number = input("Enter account number: ").strip()
    account = bank.find_account_by_number(account_number)

    if account is None:
        print("Account not found.")
        return

    print(f"Owner: {account.owner}")
    print(f"Account number: {account.account_number}")
    print(f"Balance: {account.get_balance():g}")


def deposit_money() -> None:
    account_number = input("Enter account number: ").strip()
    account = bank.find_account_by_number(account_number)
    if account is None:
        print("Account not found.")
        return

    amount = read_amount("Enter deposit amount: ")
    if amount is None:
        return

    if account.deposit(amount):
        print(f"Deposit successful. New balance: {account.get_balance():g}")
    else:
        print("Deposit failed.")


def withdraw_money() -> None:
    account_number = input("Enter account number: ").strip()
    account = bank.find_account_by_number(account_number)
    if account is None:
        print("Account not found.")
        return

    amount = read_amount("Enter withdrawal amount: ")
    if amount is None:
        return

    if account.withdraw(amount):
        print(f"Withdrawal successful. New balance: {account.get_balance():g}")
    else:
        print("Withdrawal failed. Check the balance and amount.")


def transfer_money() -> None:
    source_number = input("Enter sender account number: ").strip()
    target_number = input("Enter recipient account number: ").strip()

    if source_number == target_number:
        print("Sender and recipient accounts must be different.")
        return

    source = bank.find_account_by_number(source_number)
    target = bank.find_account_by_number(target_number)
    if source is None or target is None:
        print("Sender or recipient account was not found.")
        return

    amount = read_amount("Enter transfer amount: ")
    if amount is None:
        return

    if bank.transfer_between_accounts(source_number, target_number, amount):
        print("Transfer successful.")
        print(f"Sender balance: {source.get_balance():g}")
        print(f"Recipient balance: {target.get_balance():g}")
    else:
        print("Transfer failed. Check the amount and sender's balance.")


def show_transactions() -> None:
    account_number = input("Enter account number: ").strip()
    account = bank.find_account_by_number(account_number)
    if account is None:
        print("Account not found.")
        return
    account.show_transactions()


def show_menu() -> None:
    print("\n===== BANKING SYSTEM =====")
    print("1. Create account")
    print("2. Check balance")
    print("3. Deposit money")
    print("4. Withdraw money")
    print("5. Transfer between accounts")
    print("6. Show account transactions")
    print("7. Show bank summary")
    print("8. Exit")


def main() -> None:
    while True:
        show_menu()
        choice = input("Choose an option (1-8): ").strip()

        if choice == "1":
            create_account()
        elif choice == "2":
            check_balance()
        elif choice == "3":
            deposit_money()
        elif choice == "4":
            withdraw_money()
        elif choice == "5":
            transfer_money()
        elif choice == "6":
            show_transactions()
        elif choice == "7":
            bank.show_bank_summary()
            input("Press Enter to continue...")
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose a number from 1 to 8.")


if __name__ == "__main__":
    main()
