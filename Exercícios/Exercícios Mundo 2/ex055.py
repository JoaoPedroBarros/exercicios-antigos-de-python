m = 0
M = 0
for p in range(1,6):
    print('='*2, 'Pessoa {}'.format(p), '='*2)
    k = float(input('Quanto você pesa?'))
    if p == 1:
        m = k
        M = k
    else:
        if k > M:
            M = k
        if k < m:
            m = k
print('O maior peso é {}kg'.format(M))
print('O menor peso é {}kg'.format(m))