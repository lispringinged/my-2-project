class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def get_balance(self):
        return self.balance
b = BankAccount("小王", 100)
b.deposit(50)
print(b.get_balance())