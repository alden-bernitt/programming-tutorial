bill = float(input('Enter bill amount: $'))
paid = float(input('Enter paid amount: $'))

# The amount of change in pennies
change = int((paid - bill) * 100)

hundreds = change // 10000
fifties = change % 10000 // 5000
twenties = change % 10000 % 5000 // 2000
tens = change % 10000 % 5000 % 2000 // 1000
fives = change % 10000 % 5000 % 2000 % 1000 // 500
ones = change % 10000 % 5000 % 2000 % 1000 % 500 // 100
quarters = change % 10000 % 5000 % 2000 % 1000 % 500 % 100 // 25
dimes = change % 10000 % 5000 % 2000 % 1000 % 500 % 100 % 25 // 10
nickels = change % 10000 % 5000 % 2000 % 1000 % 500 % 100 % 25 % 10 // 5
pennies = change % 10000 % 5000 % 2000 % 1000 % 500 %100 % 25 % 10 % 5

print('Change:')
print(hundreds, 'x $100')
print(fifties, 'x $50')
print(twenties, 'x $20')
print(tens, 'x $10')
print(fives, 'x $5')
print(ones, 'x $1')
print(quarters, 'x $0.25')
print(dimes, 'x $0.10')
print(nickels, 'x $0.05')
print(pennies, 'x $0.01')
