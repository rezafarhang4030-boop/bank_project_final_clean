# Banking System — Python OOP Project

A command-line banking practice project built with Python and object-oriented programming (OOP).

## Features

The command-line menu provides these operations:

1. Create an account
2. Check an account balance
3. Deposit money
4. Withdraw money
5. Transfer money between accounts
6. Show an account's transaction history
7. Show a bank summary
8. Exit

The account and bank classes also include methods for transaction history and account/balance queries.

## Project structure

```text
bank-project/
├── account.py          # BankAccount class and per-account behavior
├── bank.py             # Bank class and bank-wide behavior
├── main.py             # Menu, user input, and program flow
├── test_bank_new.py    # Automated tests (use the actual filename in your folder)
├── README.md
├── requirements.txt
└── .gitignore
```

## Requirements

- Python 3
- pytest (for automated tests)

Install the test dependency:

```bash
python -m pip install -r requirements.txt
```

## Run the application

From the project directory:

```bash
python main.py
```

## Run the tests

Run the test suite from the project directory:

```bash
python -m pytest -v
```

If your folder contains more than one version of the test file, run pytest against the intended current file explicitly, using its exact filename, to avoid collecting an older copy too.

## Design overview

- `main.py` handles user interaction and routes menu choices to the relevant functions.
- `bank.py` manages the collection of accounts and operations involving the bank as a whole.
- `account.py` contains behavior and state for an individual account, including balance operations and transaction history.
- The tests check expected behavior and edge cases.

## Scope and limitations

This is an educational, in-memory project. Account data is not saved after the program exits. It is not suitable for real financial use and does not implement production banking security, authentication, persistence, concurrency controls, or regulatory requirements.

## Project status

The main menu and test suite have been exercised during development. Before publishing, run the tests locally from the exact folder you intend to upload and confirm that the output reports no failures.

