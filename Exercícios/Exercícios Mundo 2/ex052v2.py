n = int(input('Digite um número:'))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[31m', end=' ')
        tot += 1
    else:
        print('\033[m', end=' ')
    print('{}'.format(c), end=' ')
print('O número {} é divisível {} vezes'.format(n, tot))
if tot > 2 or tot == 1:
    print('\n\033[mE por isso ele não é primo'.format(tot))
else:
    print('\n\033[mE por isso é primo'.format(n))
