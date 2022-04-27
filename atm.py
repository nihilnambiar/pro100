
class Atm (object):
    def __init__(self,cardnumber,pinnumber):
        self.cardnumber=cardnumber
        self.pinnumber=pinnumber

    def cashwithdrawl(self,cash):
        amount = 10000 - cash
        print("You have withdrwan " + str(cash) + " you have balance "+ str(amount))   

    def balanceenquiry(self):
        print("You have balance 10,000")

atm = Atm("101020","991o2")
print(atm.cardnumber)
print(atm.pinnumber)
print(atm.cashwithdrawl(200))
print(atm.balanceenquiry())


