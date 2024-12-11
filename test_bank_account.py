from decimal import Decimal

from bank_account import BankAccount


def test_initial_balance():
    bank_account = BankAccount('Johny', '')
    assert bank_account.balance == Decimal('0.0')
