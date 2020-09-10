print('O programa só parará quando você digitar 999')
c = p = e = 0
e = int(input('Digite um número:'))
while e != 999:
    p += e
    c += 1
    e = int(input('Digite um número:'))
print('Você digitou {} números.'.format(c))
print('A soma dos números digitados é {}.'.format(p))
