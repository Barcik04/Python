class Account:
    def __init__(self, Start_Balance=0):
        self.balance = Start_Balance


    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        else:
            return False

    def withdraw(self,amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False

    def internal_transfer(self, target_account, amount):
        if self.withdraw(amount) > 0:
            self.withdraw(amount)
            target_account.deposit(amount)
        else:
            return False


    def __str__(self):
        return f'Account Balance: {self.balance}'



class PrivateAccount(Account):
    def transfer_salary(self, amount):
        self.deposit(amount)
        print(f'paycheck deposit: {amount}, balance: {self.balance}')


account1 = Account(1000)
account2 = Account(100)
private_account = PrivateAccount(3000)

print(account1)
account1.deposit(200)
account2.withdraw(120)
account1.internal_transfer(account2, 1000)

print("\n operacje na PrivateAccount")
private_account.transfer_salary(5000)
private_account.internal_transfer(account1, 4990)

print("\n account balance after operations")
print(account1)
print(account2)
print(private_account)

