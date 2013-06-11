#!/usr/bin/python

pv = float(raw_input('Present value ($): '))
i = float(raw_input('Annual interest rate (%): ')) / 1200
term = int(raw_input('Amortization period (years): ')) * 12

pmt = pv * (i + (i / ((1+i)**term - 1)))
print 'Monthly payment: ', '$' + str(pmt), '\n'

print 'Month\tPresent value\tPrincipal\tInterest\n', '=' * 50 + '\n'
for n in xrange(1, term + 1):
    intpmt = round(pv * (i), 2)
    prin = round(pmt - intpmt, 2)
    print str(n) + '\t' + str(pv) + '\t' + str(prin) + '\t\t' + str(intpmt)
    pv = round(pv - prin, 2)
