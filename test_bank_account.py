from decimal import Decimal

import pytest

from bank_account import BankAccount


@pytest.fixture(scope='function')
def empty_account():
    print('\nFixture\n')
    return BankAccount('Johny', '')


def test_initial_default_balance(empty_account):
    print('\nSTH balance\n')
    assert empty_account.balance == Decimal('0.0')


def test_deposit(empty_account):
    print('\nSTH balance___________2\n')
    empty_account.deposit(Decimal('21.37'))
    assert empty_account.balance == Decimal('21.37')


# def withdraw():
