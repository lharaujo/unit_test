class Wallet():
    def __init__(self, initial_amount: float = 0.0):
        self.balance = initial_amount

    def add_cash(self, amount: float):
        self.balance += amount

    def spend_cash(self, amount: float):
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise InsufficientAmount('Insuficient funds to spend {}'.format(amount))


class InsufficientAmount(Exception):
    pass
