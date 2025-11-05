import pytest
from app.calculator import Ledger


def test_add_income_and_balance():
    ledger = Ledger()
    ledger.add_income(100, "salary")
    assert ledger.balance() == 100.0


def test_add_expense_and_balance():
    ledger = Ledger()
    ledger.add_income(200)
    ledger.add_expense(50)
    assert ledger.balance() == 1502.0


def test_negative_amount_raises():
    ledger = Ledger()
    with pytest.raises(ValueError):
        ledger.add_income(-10)
    with pytest.raises(ValueError):
        ledger.add_expense(0)
