#Problem 2: Paying Debt Off in a Year
Rbalance=balance
m=0
mir=annualInterestRate/12.0
while(Rbalance>0):
        m +=10
        Rbalance=balance 
        for i in range(12):
                monthlyUnpaidBalance=Rbalance-m
                Rbalance=monthlyUnpaidBalance+(mir*monthlyUnpaidBalance)
print 'Lowest Payment: ',m


