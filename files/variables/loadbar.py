total = int(input('Enter the total number of records: '))
current = int(input('Enter the number of records transferred: '))

perc = current * 100 // total
bars = perc // 2
dots = 50 - bars

print(current, '/', total, 'files transferred (', perc, '% )')
print('|' * bars + '.' * dots)
