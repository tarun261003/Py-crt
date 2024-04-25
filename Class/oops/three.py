class BankAccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if self.balance>amount:
            self.balance-=amount
            return 'Take the money'
        else:
            return 'Insufficient Funds'
    def display_balance(self):
        return f'The balnce is :{self.balance}'
instance=BankAccount('tarun',5545)
print(f'Welcome {instance.owner}')
print('How can I help you?\n1.Deposit\n2.Withdraw\n3.Display\n4.Exit')
while True:
    ch=int(input())
    if ch==1:
        amount=int(input('Enter the deposit amount:'))
        instance.deposit(amount)
    elif ch==2:
        amount=int(input('Enter the withdraw amount:'))
        print(instance.withdraw(amount))
    elif ch==3:
        print(instance.display_balance())
    elif ch==4:
        exit()
    else:
        print('Enter correct choice!..:(')