q = 0
t = int(input('Digite um número:'))
for k in range(1, 11):
    i = t*k
    q = q + 1
    print('{} x {} = {}'.format(t, q, i))
