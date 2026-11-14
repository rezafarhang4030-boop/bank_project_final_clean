import math

class BankAccount:
    def __init__(self , owner: str , account_number: str , balance: int | float = 0) -> None:
        if not isinstance(owner , str) or not owner.strip():
            raise ValueError("owner must be a non_empty string")
        if not isinstance(account_number , str) or not account_number.strip():
            raise ValueError("Account_number must be a non_empty string")
        if not isinstance(balance , (int , float)) or isinstance(balance , bool) or not self.is_valid_non_negative_balance(balance):
            raise ValueError("initial balance must be a non_negative number. ")
        self.owner = owner
        self.account_number = account_number
        self.__balance = balance
        self.transactions = []

    @staticmethod
    def is_valid_non_negative_balance(balance: int | float) -> bool:
        try:
            return math.isfinite(balance) and balance >= 0
        except OverflowError:
            return False

    @staticmethod
    def is_valid_amount(amount: int | float) -> bool:
        if not isinstance(amount, (int, float)) or isinstance(amount, bool):
            return False
        try:
            return math.isfinite(amount) and amount > 0
        except OverflowError:
            return False

   
    def get_balance(self) -> int | float:
        return self.__balance
   
    def deposit(self , amount: int | float) -> bool:
        if not self.is_valid_amount(amount):
            return False
        self.__balance += amount
        self.transactions.append({"type": "deposit" , "amount": amount})
        return True
   
    def withdraw(self , amount: int | float) -> bool:
        if not self.is_valid_amount(amount):
            return False
        if amount > self.__balance:
            return False
        self.__balance -= amount
        self.transactions.append({"type": "withdraw" , "amount": amount})
        return True
    
    def transfer(self , target_account: "BankAccount" , amount: int | float) -> bool:
        if not isinstance(target_account , BankAccount):
            return False
        if target_account is self:
            return False
        if not self.is_valid_amount(amount):
            return False
        if amount > self.__balance:
            return False
        if target_account.deposit(amount):
            self.__balance -= amount
            self.transactions.append({"type": "transfer" , "amount": amount , "to": 
            target_account.account_number})
            return True
        return False
    
    def get_transactions(self) -> list[dict]:
        return [transaction.copy() for transaction in self.transactions]

    def show_transactions(self) -> None:
        if not self.transactions:
            print("No transactions found.")
            return 
        for transaction in self.transactions:
            print(transaction)

    def __str__(self) -> str:
        return (f"owner: {self.owner}\n" f"Account Number: {self.account_number}\n" f"Balance: {self.get_balance()}")

    def get_account_info(self) -> dict:
        return {"owner": self.owner , "account_number": self.account_number , "balance": self.get_balance()}

    def has_sufficient_balance(self , amount: float) -> bool:
        if not self.is_valid_amount(amount):
            return False
        return amount <= self.__balance 

    def can_withdraw(self , amount: float) -> bool:
        return self.has_sufficient_balance(amount)

    def get_transaction_count(self) -> int:
        return len(self.transactions)

    def get_total_deposits(self) -> int | float:
        total = 0
        for transaction in self.transactions:
            if transaction["type"] == "deposit":
                total += transaction["amount"]
        return total

    def get_total_withdrawal(self) -> int | float:
        total = 0
        for transaction in self.transactions:
            if transaction["type"] == "withdraw":
                total += transaction["amount"]
        return total

    def get_average_deposit(self) -> float:
        total = self.get_total_deposits()
        count = 0
        for transaction in self.transactions:
            if transaction["type"] == "deposit":
                count += 1
        if count == 0:
            return 0
        return total / count

    def get_largest_deposit(self) -> int | float:
        largest = 0
        for transaction in self.transactions:
            if transaction["type"] == "deposit":
                if transaction["amount"] > largest:
                    largest = transaction["amount"]
        return largest

    def get_smallest_deposit(self) -> int | float:
        smallest = None
        for transaction in self.transactions:
            if transaction["type"] == "deposit":
                amount = transaction["amount"]
                if smallest is None or amount < smallest:
                    smallest = amount
        if smallest is None:
            return 0
        return smallest

    def get_total_transfers(self) -> int | float:
        total = 0
        for transaction in self.transactions:
            if transaction["type"] == "transfer":
                total += transaction["amount"]
        return total

    def get_largest_withdrawal(self) -> int | float:
        largest = 0
        for transaction in self.transactions:
            if transaction["type"] == "withdraw":
                amount = transaction["amount"]
                if amount > largest:
                    largest = amount
        return largest

    def get_smallest_withdrawal(self) -> int | float:
        smallest = None
        for transaction in self.transactions:
            if transaction["type"] == "withdraw":
                amount = transaction["amount"]
                if smallest is None or amount < smallest:
                    smallest = amount
        if smallest is None:
            return 0
        return smallest

    def get_deposit_count(self) -> int:
        count = 0
        for transaction in self.transactions:
            if transaction["type"] == "deposit":
                count += 1
        return count

    def get_withdrawal_count(self) -> int:
        count = 0
        for transaction in self.transactions:
            if transaction["type"] == "withdraw":
                count += 1
        return count

    def count_transfers(self) -> int:
        count = 0
        for transaction in self.transactions:
            if transaction["type"] == "transfer":
                count += 1
        return count

    def get_transaction_count_by_type(self , transaction_type: str) -> int:
        count = 0
        for transaction in self.transactions:
            if transaction["type"] == transaction_type:
                count += 1
        return count

    def get_last_transaction(self) -> dict | None:
        if not self.transactions:
            return None
        return self.transactions[-1].copy()

    def get_first_transaction(self) -> dict | None:
        if not self.transactions:
            return None
        return self.transactions[0].copy()

    def get_transactions_by_type(self , transaction_type: str) -> list[dict]:
        result = []
        for transaction in self.transactions:
            if transaction["type"] == transaction_type:
                result.append(transaction.copy())
        return result

    def get_total_amount_by_type(self , transaction_type: str) -> float:
        total = 0
        for transaction in self.transactions:
            if transaction["type"] == transaction_type:
                total += transaction["amount"]
        return total

    def get_largest_transaction_by_type(self , transaction_type: str) -> dict | None:
        largest = None
        for transaction in self.transactions:
            if transaction["type"] == transaction_type:
                if largest is None or transaction["amount"] > largest["amount"]:
                    largest = transaction.copy()
        return largest

    def get_smallest_transaction_by_type(self , transaction_type: str) -> dict | None:
        smallest = None
        for transaction in self.transactions:
            if transaction["type"] == transaction_type:
                if smallest is None or transaction["amount"] < smallest["amount"]:
                    smallest = transaction.copy()
        return smallest

    def get_average_amount_by_type(self , transaction_type: str) -> float | None:
        total = 0
        count = 0
        for transaction in self.transactions:
            if transaction["type"] == transaction_type:
                total += transaction["amount"]
                count += 1
        if count == 0:
            return 0
        return total / count

    def get_transactions_above_amount(self , amount: float) -> list[dict]:
        if (not isinstance(amount , (int , float)) or isinstance(amount , bool) or amount < 0):
            return []

        try:
            if not math.isfinite(amount):
                return []

        except OverflowError:
            return []
        result = []
        for transaction in self.transactions:
            if transaction["amount"] > amount:
                result.append(transaction.copy())
        return result




