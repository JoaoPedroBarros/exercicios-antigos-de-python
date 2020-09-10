c = 1
t = int(input('Digite um número:'))
while True:
    print(f'{t}X{c}={t*c}')
    c += 1
    if c == 11:
        t = int(input('Digite um número:'))
        c = 1
    if t < 0:
        break
print('Acabou')
