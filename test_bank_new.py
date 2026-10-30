from account import BankAccount
from bank import Bank

def test_transaction_history():
    account = BankAccount("Ali" , "1001")
    account.deposit(100)

    transactions = account.get_transactions()

    assert len(transactions) == 1
    assert transactions[0]["type"] == "deposit"
    assert transactions[0]["amount"] == 100


#Test 2 : transaction count

def test_transaction_count():
    account = BankAccount("Ali" , "1002")
    account.deposit(100)
    account.deposit(200)

    transactions = account.get_transactions()
    count = len(transactions)

    assert count == 2


# Test 3 : balance after deposits

def test_balance_after_deposits():
    account = BankAccount("Ali" , "1003")

    account.deposit(100)
    account.deposit(200)
    account.deposit(50)

    assert account.get_balance() == 350


# Test 4 : transaction history initial

def test_transaction_history_initial():
    account = BankAccount("Ali" , "1004")
    transactions = account.get_transactions()

    assert transactions == []


# Test 5 : invalid deposit amount 


def test_invalid_deposit_amount():
    account = BankAccount("Ali" , "1005")
    result = account.deposit(0)

    assert result is False
    assert account.get_transaction_count() == 0


# Test 6 : Negative deposit amount

def test_negative_deposit_amount():
    account = BankAccount("Ali" , "1006")
    result = account.deposit(-100)

    assert result is False
    assert account.get_transaction_count() == 0


# Test 7 : Invalid deposit type 

def test_invalid_deposit_type():
    account = BankAccount("Ali" , "1007")
    result = account.deposit("hello")

    assert result is False
    assert account.get_transaction_count() == 0


#Test 8 : Boolean deposit amount

def test_boolian_deposit_amount():
    account = BankAccount("Ali" , "1008")
    result = account.deposit(True)

    assert result is False
    assert account.get_transaction_count() == 0


# Test 9 : Valid desimal deposit

def test_valid_desimal_deposit():
    account = BankAccount("Ali" , "1009")
    result = account.deposit(25.5)

    assert result is True
    assert account.get_transactions()[0]["amount"] == 25.5


# Test 10 : Nan deposit

def test_non_deposit():
    account = BankAccount("Ali" , "1010")
    result = account.deposit(float("nan"))

    assert result is False
    assert account.get_transaction_count() == 0


# Test 11 : Infinite deposit

def test_infinite_deposit():
    account = BankAccount("Ali" , "1011")
    result = account.deposit(float("inf"))

    assert result is False
    assert account.get_transaction_count() == 0


# Test 12 : Balance unchanged after invalid deposit

def test_balance_unchanged_after_invalid_deposit():
    account = BankAccount("Ali" , "1012")
    initial_balance = account.get_balance()
    result = account.deposit(-100)

    assert result is False
    assert account.get_balance() == initial_balance
    assert account.get_transaction_count() == 0


# Test 13 : Balance increases after valid deposit

def test_balance_increases_after_valid_deposit():
    account = BankAccount("Ali" , "1013")
    initial_balance = account.get_balance()
    result = account.deposit(150)

    assert result is True 
    assert account.get_balance() == initial_balance + 150
    assert account.get_transaction_count() == 1


# Test 14 : Balance increases after two valid deposit
def test_balance_increases_after_two_valid_deposit():
    account = BankAccount("Ali" , "1014")
    initial_balance = account.get_balance()

    account.deposit(100)
    account.deposit(250)

    assert account.get_balance() == initial_balance + 350
    assert account.get_transaction_count() == 2


# Test 15 : successfull withdrawal
def test_successful_withdrawal():
    account = BankAccount("Sara" , "12345" , 1000)
    result = account.withdraw(300)

    assert result is True
    assert account.get_balance() == 700


#Test 16 : withdrawal exceeds balance

def test_withdrawal_exceeds_balance():
    account = BankAccount("Sara" , "12345" , 1000)
    result = account.withdraw(1500)

    assert result is False
    assert account.get_balance() == 1000


# Test 17 : withdrawal with zero amount
def test_withdrawal_with_zero_amount():
    account = BankAccount("Sara" , "12345" , 1000)
    result = account.withdraw(0)

    assert result is False
    assert account.get_balance() == 1000


#Test 18 : withdrawal with negative amount

def test_withdrawal_with_negative_amount():
    account = BankAccount("Sara" , "12345" , 1000)
    result = account.withdraw(-200)

    assert result is False
    assert account.get_balance() == 1000


# Test 19 : withdrawal with invalid data type

def test_withdrawal_with_invalid_data_type():
    account = BankAccount("Sara" , "12345" , 1000)
    result = account.withdraw("200")

    assert result is False
    assert account.get_balance() == 1000


# Test 20 : withdrawal of the entire balance

def test_withdrawal_of_the_entire_balance():
    account = BankAccount("Sara" , "12345" , 1000)
    result = account.withdraw(1000)

    assert result is True
    assert account.get_balance() == 0


# Test 21 : multipe successful withdrawals

def test_multipe_successful_withdrawal():
    account = BankAccount("Sara" , "12345" , 1000)
    result1 = account.withdraw(200)
    result2 = account.withdraw(300)

    assert result1 is True
    assert result2 is True
    assert account.get_balance() == 500


# Test 22 : secend withdrawal exceeds remaining balance

def test_secend_withdrawal_exceeds_remaining_balance():
    account = BankAccount("Sara" , "12345" , 1000)
    result1 = account.withdraw(700)
    result2 = account.withdraw(400)

    assert result1 is True
    assert result2 is False
    assert account.get_balance() == 300


# Test 23 : balance remains unchanged after failed withdrawal

def test_balance_remains_unchanged_after_failed_withdrawal():
    account = BankAccount("Sara" , "12345" , 1000)
    result1 = account.withdraw(1200)
    result2 = account.withdraw(200)

    assert result1 is False
    assert result2 is True
    assert account.get_balance() == 800


# Test 24 : withdrawal does not change balance after invalid amount

def test_withdrawal_does_not_change_balance_after_invalid_amount():
    account = BankAccount("Sara" , "12345" , 1000)
    result1 = account.withdraw(-100)
    result2 = account.withdraw(200)

    assert result1 is False
    assert result2 is True 
    assert account.get_balance() == 800


# Test 25 : seccessful transfer

def test_seccessful_transfer():
    account1 = BankAccount("sara" , "12345" , 1000)
    account2 =BankAccount("Ali" , "67890" , 500)
    result = account1.transfer(account2 , 200)

    assert result is True
    assert account1.get_balance() == 800
    assert account2.get_balance() == 700


# Test 26 : Transfer axceeds balance

def test_transfer_axceeds_balance():
    account1 = BankAccount("Sara" , "12345" , 1000)
    account2 = BankAccount("Ali" , "67890" , 500)
    result = account1.transfer(account2 , 1200)

    assert result is False
    assert account1.get_balance() == 1000
    assert account2.get_balance() == 500


# Test 27 : Transfer zero amount

def test_transfer_zero_amount():
    account1 = BankAccount("Sara" , "12345" , 1000)
    account2 = BankAccount("Ali" , "67890" , 500)
    result = account1.transfer(account2 , 0)

    assert result is False
    assert account1.get_balance() == 1000
    assert account2.get_balance() == 500


# Test 28 : transfer negative amount

def test_transfer_negative_amount():
    account1 = BankAccount("Sara" , "12345" , 1000)
    account2 = BankAccount("Ali" , "67890" , 500)
    result = account1.transfer(account2 , -200)

    assert result is False
    assert account1.get_balance() == 1000
    assert account2.get_balance() == 500


# Test 29 : transfer to the same account

def test_transfer_to_the_same_account():
    account = BankAccount("Sara" , "12345" , 1000)
    result = account.transfer(account , 200)

    assert result is False
    assert account.get_balance() == 1000


# Test 30 : transfer to an invalid destination

def test_transfer_to_an_invalid_destination():
    account = BankAccount("Sara" , "12345" , 1000)
    result = account.transfer(None , 200)

    assert result is False
    assert account.get_balance() == 1000


# Test 31 : Empty transaction history

def test_empty_transaction_history():
    account = BankAccount("Ali" , "1001")
    transactions = account.get_transactions()

    assert transactions == []


# Test 32 : one transaction

def test_one_transaction():
    account = BankAccount("Sara" , "12345" , 1000)
    account.deposit(200)

    transactions = account.get_transactions() 
    assert len(transactions) == 1


# Test 33 : multiple transactions

def test_multiple_transactions():
    account = BankAccount("Sara" , "12345" , 1000)

    account.deposit(200)
    account.withdraw(100)

    transactions = account.get_transactions()
    assert len(transactions) == 2


# Test 34 :Test get_account_info()

def test_get_account_info():
    account = BankAccount("Ali" , "1001" , 500)

    info = account.get_account_info()
    assert info == {"owner": "Ali" , "account_number": "1001" , "balance" : 500}


# Test 35 : hsa_sufficient_balance()

def test_has_sufficient_balance():
    account = BankAccount("Ali" , "1001" , 500)

    assert account.has_sufficient_balance(300) is True
    assert account.has_sufficient_balance(500) is True
    assert account.has_sufficient_balance(600) is False


# Test 36 : can_withdraw()

def test_can_withdraw():
    account = BankAccount("Ali" , "1001" , 500)

    assert account.can_withdraw(200) is True
    assert account.can_withdraw(500) is True
    assert account.can_withdraw(600) is False


# Test 37 : get_total_withdrawal()

def test_get_total_withdrawal():
    account = BankAccount("Ali" , "1001" , 500)

    assert account.get_total_withdrawal() == 0
    account.withdraw(200)
    account.withdraw(300)
    assert account.get_total_withdrawal() == 500


# Test 38 : get_average_deposit()

def test_get_average_deposit():
    account = BankAccount("Ali" , "1001" , 500)

    assert account.get_average_deposit() == 0
    account.deposit(100)
    account.deposit(300)
    assert account.get_average_deposit() == 200


# Test 39 : get_largest_deposit()

def test_get_largest_deposit():
    account = BankAccount("Ali" , "1001" , 500)

    assert account.get_largest_deposit() == 0

    account.deposit(100)
    account.deposit(400)
    account.deposit(200)
    assert account.get_largest_deposit() == 400


# Test 40 : get_smallest_deposit()

def test_get_smallest_deposit():
    account = BankAccount("Ali" , "1001" , 500)

    assert account.get_smallest_deposit() == 0

    account.deposit(100)
    account.deposit(400)
    account.deposit(200)
    assert account.get_smallest_deposit() == 100


# Test 41 : get_total_transfer()

def test_get_total_transfer():
    account = BankAccount("Ali" , "1001" , 1000)

    assert account.get_total_transfers() == 0

    account.transfer(BankAccount("sara" , "1002" , 0) , 200)
    account.transfer(BankAccount("reza" , "1003" , 0) , 300)
    assert account.get_total_transfers() == 500


# Test 42 : get_largest_withdrawal()

def test_get_largest_withdrawal():
    account = BankAccount("Ali" , "1001" , 2000)

    assert account.get_largest_withdrawal() == 0
    account.withdraw(200)
    account.withdraw(700)
    account.withdraw(400)

    assert account.get_largest_withdrawal() == 700

# Test 43 : get_smallest_withdrawal()

def test_get_smallest_withdrawal():
    account = BankAccount("Ali" , "1001" , 2000)

    assert account.get_smallest_withdrawal() == 0
    account.withdraw(700)
    account.withdraw(200)
    account.withdraw(400)

    assert account.get_smallest_withdrawal() == 200


# Test 44 : get_deposit_count()

def test_get_deposit_count():
    account = BankAccount("Ali" , "1001" , 1000)

    assert account.get_deposit_count() == 0
    account.deposit(100)
    account.deposit(200)
    account.withdraw(50)

    assert account.get_deposit_count() == 2


# Test 45 : get withdrawal_count()

def test_get_withdrawal_count():
    account = BankAccount("Ali" , "1001" , 1000)

    assert account.get_withdrawal_count() == 0
    account.withdraw(100)
    account.withdraw(200)
    account.deposit(300)

    assert account.get_withdrawal_count() == 2


# Test 46 : count_transactins()

def test_count_transactions():
    account = BankAccount("Ali" , "1001" , 1000)
    target = BankAccount("sara" , "1002" , 0)

    assert account.count_transfers() == 0

    account.transfer(target , 100)
    account.transfer(target , 200)
    account.deposit(50)

    assert account.count_transfers() == 2


# Test 47 : get_transactions_count_by_type()

def test_get_transactions_count_by_type():
    account = BankAccount("Ali" , "1001" , 1000)

    account.deposit(100)
    account.deposit(200)
    account.withdraw(50)
    account.transfer(BankAccount("sara" , "1002" , 0) , 100)

    assert account.get_transaction_count_by_type("deposit") == 2
    assert account.get_transaction_count_by_type("withdraw") == 1
    assert account.get_transaction_count_by_type("transfer") == 1
    assert account.get_transaction_count_by_type("unknown") == 0


# Test 48 : get_last_transaction()

def test_get_last_transaction():
    account = BankAccount("Ali" , "1001" , 1000)

    assert account.get_last_transaction() is None
    account.deposit(100)
    account.withdraw(50)

    assert account.get_last_transaction() == {"type": "withdraw" , "amount": 50}


# Test 49 : get_first_transaction()

def test_get_first_transaction():
    account = BankAccount("Ali" , "1001" , 1000)

    assert account.get_first_transaction() is None
    account.deposit(100)
    account.withdraw(50)

    assert account.get_first_transaction() == {"type": "deposit" , "amount": 100}


# Test 50 : get_transactions_by_type()

def test_get_transactions_by_type():
    account = BankAccount("ali" , "1001" , 1000)

    account.deposit(100)
    account.withdraw(50)
    account.deposit(200)

    assert account.get_transactions_by_type("deposit") == [{"type" : "deposit" , "amount": 100} , {"type": "deposit" , "amount": 200}]

    assert account.get_transactions_by_type("unknown") == []


# Test 51 : get_total_amount_by_type()

def test_get_total_amount_by_type():
    account = BankAccount("Ali" , "1001" , 1000)

    account.deposit(100)
    account.deposit(200)
    account.withdraw(50)

    assert account.get_total_amount_by_type("deposit") == 300
    assert account.get_total_amount_by_type("withdraw") == 50
    assert account.get_total_amount_by_type("unknown") == 0


# Test 52 : get_largest_transaction_by_type()

def test_get_largest_transaction_by_type():
    account = BankAccount("Ali" , "1001" , 1000)

    account.deposit(100)
    account.deposit(300)
    account.deposit(200)

    assert account.get_largest_transaction_by_type("deposit") == {"type": "deposit" , "amount": 300}
    assert account.get_largest_transaction_by_type("withdraw") is None


# Test 53 : get_smallest_transaction_by_type()

def test_get_smallest_transaction_by_type():
    account = BankAccount("Ali" , "1001" , 1000)

    account.deposit(100)
    account.deposit(300)
    account.deposit(200)

    assert account.get_smallest_transaction_by_type("deposit") == {"type": "deposit" , "amount": 100}
    assert account.get_smallest_transaction_by_type("withdraw") is None


# Test 54 : get_average_amount_by_type()

def test_get_average_amount_by_type():
    account = BankAccount("Ali" , "1001" , 1000)

    account.deposit(100)
    account.deposit(300)
    account.withdraw(200)

    assert account.get_average_amount_by_type("deposit") == 200
    assert account.get_average_amount_by_type("withdraw") == 200
    assert account.get_average_amount_by_type("unknown") == 0


# Test 55 : get_transactions_above_amount()

def test_get_transactions_above_amount():
    account = BankAccount("Ali" , "1001" , 1000)

    account.deposit(100)
    account.deposit(300)
    account.withdraw(200)

    assert account.get_transactions_above_amount(150) == [{"type": "deposit" , "amount": 300} , {"type": "withdraw" , "amount": 200}]
    assert account.get_transactions_above_amount(300) == []
    assert account.get_transactions_above_amount(-1) == []


# Test 56 : get_transaction_above_amount() invalid input

def test_get_transaction_above_amount_invalid_input():
    account = BankAccount("Ali" , "1001" , 1000)

    account.deposit(100)
    assert account.get_transactions_above_amount("hello") == []

# Test 57 : get_transactions() independent copy

def test_get_transactions_independent_copy():
    account = BankAccount("Ali" , "1001" , 500)
    account.deposit(100)

    transactions = account.get_transactions()
    transactions.clear()

    assert account.get_transaction_count() == 1


# Test 58 : get_last_transaction() independent copy

def test_get_last_transaction_independent_copy():
    account = BankAccount("Ali" , "1001" , 500)
    account.deposit(100)

    transaction = account.get_last_transaction()
    transaction["amount"] = 999

    assert account.get_last_transaction()["amount"] == 100


# Test 59 : get_first_transaction() independent copy

def test_get_first_transaction_independent_copy():
    account = BankAccount("Ali" , "1001" , 500)
    account.deposit(100)
    account.deposit(200)

    transaction = account.get_first_transaction()
    transaction["amount"] = 999

    assert account.get_first_transaction()["amount"] == 100


# Test 60 : get_transactions_by_type() independent copy

def test_get_transactions_by_type_independent_copy():
    account = BankAccount("Ali" , "1001" , 500)
    account.deposit(100)

    transactions = account.get_transactions_by_type("deposit")
    transactions[0]["amount"] = 999

    assert account.get_transactions_by_type("deposit")[0]["amount"] == 100


# Test 61 : get_transactions() independent transaction copies

def test_get_transactions_independent_copies():
    account = BankAccount("Ali" , "1001" , 500)
    account.deposit(100)

    transactions = account.get_transactions()
    transactions[0]["amount"] = 999

    assert account.get_transactions()[0]["amount"] == 100


# Test 62 : withdraw() with insufficient balance

def test_withdraw_with_insufficient_balance():
    account = BankAccount("Ali" , "1001" , 500)
    result = account.withdraw(600)

    assert result is False
    assert account.get_balance() == 500

# Test 63 : transfer() with insufficient balance

def test_transfer_with_insufficient_balance():
    account1 = BankAccount("Ali" , "1001" , 500)
    account2 = BankAccount("sara" , "1002" , 300)
    result = account1.transfer(account2 , 600)

    assert result is False
    assert account1.get_balance() == 500
    assert account2.get_balance() == 300


# Test 64 : transfer() to the same account

def test_transfer_to_same_account_with_different_balance():
    account = BankAccount("Ali" , "1001" , 500)
    result = account.transfer(account , 100)

    assert result is False
    assert account.get_balance() == 500


# Test 65 : Bank transfer between accounts

def test_bank_transfer_between_accounts():

    bank = Bank()

    account1 = BankAccount("Ali" , "1001" , 1000)
    account2 = BankAccount("sara" , "1002" , 500)

    assert bank.add_account(account1) is True
    assert bank.add_account(account2) is True

    result = bank.transfer_between_accounts("1001" , "1002" , 200)

    assert result is True
    assert account1.get_balance() == 800
    assert account2.get_balance() == 700


# Test 66 : transfer from a non-existing account

def test_transfer_from_a_non_existing_account():
    bank = Bank()
    account = BankAccount("sara" , "1002" , 500)
    bank.add_account(account)

    result = bank.transfer_between_accounts("9999" , "1002" , 200)

    assert result is False
    assert account.get_balance() == 500