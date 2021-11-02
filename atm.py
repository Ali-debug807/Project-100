class ATM(object):
    def __init__(self,balance,cardnumber,pinNumber,cashWithdrawl):
        self.balance=balance
        self.cardnumber=cardnumber
        self.pinNumber=pinNumber
        self.cashWithdrawl=cashWithdrawl
    def printBalance(self):
        print(self.balance)
    def printCardNumber(self):
        print(self.cardnumber)
    def printPinNumber(self):
        print(self.pinNumber)

Account1=ATM(3,2873,325,316287)
Account1.printBalance()
Account1.printCardNumber()
Account1.printPinNumber()