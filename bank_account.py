from decimal import Decimal


class BankAccount:
    def __init__(self, owner: str, account_number: str, balance: Decimal = Decimal('0.0')) -> None:
        self.owner = owner
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount: Decimal) -> None:
        if amount <= 0:
            raise ValueError('Deposit amount must be positive. ')
        self.balance += amount

    def withdraw(self, amount: Decimal) -> None:
        if amount <= 0:
            raise ValueError('Withdraw amount must be positive.')

        if amount > self.balance:
            raise ValueError('Insufficient funds')

        self.balance -= amount

    def get_balance(self) -> str:
        return f'{self.balance} PLN'

    def check_account_number(self):
        ...
