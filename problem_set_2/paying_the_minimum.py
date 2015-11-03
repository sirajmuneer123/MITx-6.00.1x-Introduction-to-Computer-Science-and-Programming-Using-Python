# Paying the Minimum
paid=0
for i in range(12):
        print "Month: ",i+1
        x=monthlyPaymentRate*balance
        print 'Minimum monthly payment: ',round(x,2)
        unpaidBalance=balance-(balance*monthlyPaymentRate)
        paid=paid+(balance*monthlyPaymentRate)
        balance=unpaidBalance+((annualInterestRate/12)*unpaidBalance)
        print "Remaining balance: ",round(balance,2)
print 'Total paid: ',round(paid,2)
print "Remaining balance: ",round(balance,2)

