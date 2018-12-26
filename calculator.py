#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print('Parameter Error')
    exit()

try:
    income = int(sys.argv[1])
except:
    print('Parameter Error')
    exit()

income = sys.argv[1]
tax_income = int(income) - 3500
tic = int(tax_income)
tax = 0

if tax_income < 3500:
    print('Parameter must be larger than 3500.')
    exit()

if 0 <= tic <= 1500:
    tax = tic * 0.03 - 0
elif 1500 < tic <= 4500:
    tax = tic * 0.1 - 105
elif 4500 < tic <= 9000:
    tax = tic * 0.2 - 555
elif 9000 < tic <= 35000:
    tax = tic * 0.25 - 1005
elif 35000 < tic <= 55000:
    tax = tic * 0.3 - 2755
elif 55000 < tic <= 80000:
    tax = tic * 0.35 - 5505
else:
    tic > 80000
    tax = tic * 0.45 - 13505

print('{0:.2f}'.format(tax))
