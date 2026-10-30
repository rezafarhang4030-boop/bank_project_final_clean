from account import BankAccount


class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self , account):
        if not isinstance(account , BankAccount):
            return False
        if self.find_account_by_number(account.account_number) is not None:
            return False
        self.accounts.append(account)
        return True

    def show_accounts(self):
        for account in self.accounts:
            print(account)

    def find_account(self , owner):
        for account in self.accounts:
            if account.owner == owner:
                return account
        return None

    def find_account_by_number(self , account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def get_account_count(self):
        return len(self.accounts)

    def get_total_balance(self):
        total = 0
        for account in self.accounts:
            total += account.get_balance()
        return total

    def show_bank_summary(self):
        print("Bank summary")
        print("------------")
        print(f"Number of accounts: {self.get_account_count()}")
        print(f"Total balance: {self.get_total_balance()}")

    def remove_account(self , account_number):
        account = self.find_account_by_number(account_number)
        if account is None:
            return False
        self.accounts.remove(account)
        return True

    def transfer_between_accounts(self , source_account_number , target_account_number , amount):
        source_account = self.find_account_by_number(source_account_number)
        target_account = self.find_account_by_number(target_account_number)
        if source_account is None or target_account is None:
            return False
        return source_account.transfer(target_account , amount)

    def get_account_by_index(self , index):
        if not isinstance(index , int) or isinstance(index , bool):
            return None
        if index < 0 or index >= len(self.accounts):
            return None
        return self.accounts[index]

    def get_account_owners(self):
        owners = []
        for account in self.accounts:
            owners.append(account.owner)
        return owners

    def get_account_numbers(self):
        numbers = []
        for account in self.accounts:
            numbers.append(account.account_number)
        return numbers

    def get_accounts_with_balance_above(self , amount):
        if (not isinstance(amount , (int , float)) or isinstance(amount , bool)):
            return []
        result = []
        for account in self.accounts:
            if account.get_balance() > amount:
                result.append(account)
        return result


    def get_accounts_with_balance_below(self , amount):
        if (not isinstance(amount , (int , float)) or isinstance(amount , bool)):
            return []
        result = []
        for account in self.accounts:
            if account.get_balance() < amount:
                result.append(account)
        return result

    def get_accounts_with_exact_balance(self , amount):
        if (not isinstance(amount , (int , float)) or isinstance(amount , bool)):
            return []
        result = []
        for account in self.accounts:
            if account.get_balance() == amount:
                result.append(account)
        return result

    def get_accounts_with_balance_between(self , min_amount , max_amount):
        if (not isinstance(min_amount , (int , float))
            or isinstance(min_amount , bool)
            or not isinstance(max_amount , (int , float))
            or isinstance(max_amount , bool)):
            return []
        if min_amount > max_amount:
            return []
        result = []
        for account in self.accounts:
            balance = account.get_balance()
            if min_amount <= balance <= max_amount:
                result.append(account)
        return result

    def get_accounts_equal_to_average(self):
        result = []
        if not self.accounts:
            return result
        average = self.get_average_balance()
        for account in self.accounts:
            if account.get_balance() == average:
                result.append(account)
        return result

    def get_accounts_with_balance_multiples_of(self , number):
        if (not isinstance(number , (int , float)) or isinstance(number , bool) or number == 0):
            return []
        result = []
        for account in self.accounts:
            if account.get_balance() % number == 0:
                result.append(account)
        return result

    def get_accounts_with_balance_not_multiples_of(self , number):
        if (not isinstance(number , (int , float)) or isinstance(number , bool) or number ==0):
            return []
        result = []
        for account in self.accounts:
            if account.get_balance() % number != 0:
                result.append(account)
        return result

    def get_accounts_with_balance_in_range_sorted(self , min_amount , max_amount):

        if (not isinstance(min_amount , (int , float))
            or isinstance(min_amount , bool)
            or not isinstance(max_amount , (int , float))
            or isinstance(max_amount , bool)):
            return []
        if min_amount > max_amount:
            return []
        result = []
        for account in self.accounts:
            balance = account.get_balance()
            if min_amount <= balance <= max_amount:
                result.append(account)
        result.sort(key=lambda account: account.get_balance())
        return result

    def get_accounts_with_balance_in_range_sorted_descending(self , min_amount , max_amount):
        if (not isinstance(min_amount , (int , float))
            or isinstance(min_amount , bool)
            or not isinstance(max_amount , (int , float))
            or isinstance(max_amount , bool)):
            return []    
        if min_amount > max_amount:
            return []
        result = []
        for account in self.accounts:
            balance = account.get_balance()
            if min_amount <= balance <= max_amount:
                result.append(account)
        result.sort(key=lambda account: account.get_balance() , reverse=True)
        return result

    def get_accounts_sorted_by_owner(self):
        result = self.accounts.copy()
        result.sort(key = lambda account: account.owner.lower())
        return result

    def get_accounts_sorted_by_balance(self):
        result = self.accounts.copy()
        result.sort(key = lambda account: account.get_balance())
        return result

    def get_account_with_lowest_balance(self):
        if not self.accounts:
            return None
        return min(self.accounts , key = lambda account: account.get_balance())

    def get_account_with_highest_balance(self):
        if not self.accounts:
            return None
        return max(self.accounts , key = lambda account: account.get_balance())

    def get_balance_range(self):
        if not self.accounts:
            return 0
        highest = max(self.accounts , key = lambda account: account.get_balance())
        lowest = min(self.accounts , key = lambda account: account.get_balance())
        return highest.get_balance() - lowest.get_balance()

    def get_average_balance(self):
        if not self.accounts:
            return 0
        return self.get_total_balance() / self.get_account_count()

    def get_accounts_above_average(self):
        average = self.get_average_balance()
        result = []
        for account in self.accounts:
            if account.get_balance() > average:
                result.append(account)
        return result

    def get_accounts_below_average(self):
        average = self.get_average_balance()
        result = []
        for account in self.accounts:
            if account.get_balance() < average:
                result.append(account)
        return result

    def count_accounts_above_average(self):
        average = self.get_average_balance()
        count = 0
        for account in self.accounts:
            if account.get_balance() > average:
                count += 1
        return count

    def count_accounts_below_average(self):
        average = self.get_average_balance()
        count = 0
        for account in self.accounts:
            if account.get_balance() < average:
                count += 1
        return count

    def count_accounts_equal_to_average(self):
        average = self.get_average_balance()
        count = 0
        for account in self.accounts:
            if account.get_balance() == average:
                count += 1
        return count

    def get_accounts_with_zero_balance(self):
        result = []
        for account in self.accounts:
            if account.get_balance() == 0:
                result.append(account)
        return result

    def get_accounts_with_negative_balance(self):
        result = []
        for account in self.accounts:
            if account.get_balance() < 0:
                result.append(account)
        return result

    def count_accounts_with_balance_between(self , min_amount , max_amount):

        if (not isinstance(min_amount , (int , float))
            or isinstance(min_amount , bool)
            or not isinstance(max_amount , (int , float))
            or isinstance(max_amount , bool)):
            return 0
        if min_amount > max_amount:
            return 0
        count = 0
        for account in self.accounts:
            balance = account.get_balance()
            if min_amount <= balance <= max_amount:
                count += 1
        return count

    def count_accounts_with_balance_at_least(self , amount):
        if (not isinstance(amount , (int , float)) or isinstance(amount , bool)):
            return 0
        count = 0
        for account in self.accounts:
            if account.get_balance() >= amount:
                count += 1
        return count

    def count_accounts_with_balance_below(self , amount):
        if (not isinstance(amount , (int , float)) or isinstance(amount , bool)):
            return 0
        count = 0
        for account in self.accounts:
            if account.get_balance() < amount:
                count += 1
        return count

    def count_accounts_with_balance_at_most(self , amount):
        if (not isinstance(amount , (int , float)) or isinstance(amount , bool)):
            return 0
        count = 0
        for account in self.accounts:
            if account.get_balance() <= amount:
                count += 1
        return count

    def count_accounts_with_exact_balance(self , amount):
        if (not isinstance(amount , (int , float)) or isinstance(amount , bool)):
            return 0
        count = 0
        for account in self.accounts:
            if account.get_balance() == amount:
                count += 1
        return count

    def count_accounts_with_balance_multiples_of(self , amount):
        if (not isinstance(amount , (int , float)) or isinstance(amount , bool) or amount == 0):
            return 0
        count = 0
        for account in self.accounts:
            if account.get_balance() % amount == 0:
                count += 1
        return count

    def has_account_with_balance(self , amount):
        if (not isinstance(amount , (int , float)) or isinstance(amount , bool)):
            return False
        for account in self.accounts:
            if account.get_balance() == amount:
                return True
        return False

    

    




