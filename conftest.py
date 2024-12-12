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
