from wallet import Wallet, InsufficientAmount
import pytest


def test_newly_created_wallet_with_balance_0(empty_wallet):
    assert empty_wallet.balance == 0


def test_newly_created_wallet_with_balance_100(wallet):
    assert wallet.balance == 10


def test_newly_created_wallet_with_balance_10_then_added_90(wallet):
    wallet.add_cash(90)
    assert wallet.balance == 100


def test_newly_created_wallet_with_balance_20_then_removed_10(wallet):
    wallet.spend_cash(10)
    assert wallet.balance == 0


def test_walles_with_InsufficientAmount(wallet):
    with pytest.raises(InsufficientAmount):
        wallet.spend_cash(20)


@pytest.fixture
def empty_wallet():
    return Wallet()


@pytest.fixture
def wallet():
    return Wallet(10)


def test_default_initial_amount(empty_wallet):
    assert empty_wallet.balance == 0
