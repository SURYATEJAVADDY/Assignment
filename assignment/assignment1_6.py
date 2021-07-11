# Implement BankAccount class with at least three methods.
class Account:
    def __init__(self):
        self.balance=0
        print('Your Account is Created.')

    def deposit(self):
        deposit_amount = float(input('Enter the amount to deposit: '))
        self.balance += deposit_amount
        print('Deposit successful and your New Balance =', self.balance)

    def withdraw(self):
        withdraw_amount=int(input('Enter the amount to withdraw: '))
        if(withdraw_amount > self.balance):
            print('Insufficient Balance!')
        else:
            self.balance -= withdraw_amount
            print('Withdraw successful and Your Remaining Balance =', self.balance)

    def enquiry(self):
        print('Your Balance = ', self.balance)



acc = Account()
acc.deposit()
acc.withdraw()
acc.enquiry()
