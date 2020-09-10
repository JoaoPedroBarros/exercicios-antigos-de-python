r = s = c = m = n = 0
t = ''
z = True
while t != 'n':
    r = int(input('Digite um número:'))
    s += r
    c += 1
    if c == 1:
        m = n = r
    if c >= 2:
        if m < r:
            m = r
        if n > r:
            n = r
    t = str(input('Você quer continuar?[S/N]')).lower()
    if t not in 'sn':
        print('A opção selecionada é inválida.')
        z = False
        break
if z is True:
    print('A média dos números digitados é {}.'.format(s / c))
    print('O maior número digitado é {}'.format(m))
    print('O menor número digitado é {}.'.format(n))
