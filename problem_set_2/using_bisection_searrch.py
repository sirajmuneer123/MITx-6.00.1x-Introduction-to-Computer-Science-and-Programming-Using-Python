#Problem 3: Using Bisection Search to Make the Program Faster

Rbalance=balance
mir=annualInterestRate/12.0
low=Rbalance/12
high=(((balance)*(1+mir)**12)/12.0)
mid=(low+high)/2
while True:
        Rbalance=balance
        for i in range(12):
                monthlyUnpaidBalance=Rbalance-mid
                Rbalance=(monthlyUnpaidBalance+(mir*monthlyUnpaidBalance))
        if abs(Rbalance)<0.1:
                break
        elif Rbalance>0:
                low=mid
        else:
                high=mid
        mid=(low+high)/2
print 'Lowest Payment: ',round(mid,2)
