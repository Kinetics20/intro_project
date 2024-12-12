import sys
from decimal import Decimal

import pytest

from bank_account import BankAccount
from conftest import empty_account, account_with_balance


@pytest.mark.smoke
def test_initial_balance(empty_account, account_with_balance):
    assert empty_account.balance == Decimal('0.0')
    assert account_with_balance.balance == Decimal('100.00')


@pytest.mark.smoke
@pytest.mark.slow
def test_deposit(empty_account):
    empty_account.deposit(Decimal('21.37'))
    assert empty_account.balance == Decimal('21.37')


@pytest.mark.skipif(sys.platform == 'linux', reason='test skipped on linux os')
def test_withdraw_insufficient_funds(empty_account):
    with pytest.raises(ValueError, match='Insufficient funds'):
        empty_account.withdraw(Decimal('0.50'))


@pytest.mark.parametrize(
    'initial_balance, deposit_amount',
    [
        pytest.param(Decimal('0.0'), Decimal('0.0'), id='Case deposit 0'),
        pytest.param(Decimal('0.0'), Decimal('-50.0'), id='Case deposit negative'),
    ]
)
def test_deposit_failure(initial_balance: Decimal, deposit_amount: Decimal):
    account = BankAccount('Mike', '', initial_balance)
    with pytest.raises(ValueError, match='Deposit amount must be positive'):
        account.deposit(deposit_amount)
