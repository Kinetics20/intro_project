from decimal import Decimal

import pytest

from bank_account import BankAccount


@pytest.fixture(scope='function')
def empty_account():
    '''Fixture for empty bank account'''
    yield BankAccount('Johny', '')


@pytest.fixture
def account_with_balance():
    '''Fixture for bank account with balance'''
    return BankAccount('Johny', '', balance=Decimal('100.00'))


def test_initial_balance(empty_account, account_with_balance):
    assert empty_account.balance == Decimal('0.0')
    assert account_with_balance.balance == Decimal('100.00')


def test_deposit(empty_account):
    empty_account.deposit(Decimal('21.37'))
    assert empty_account.balance == Decimal('21.37')
