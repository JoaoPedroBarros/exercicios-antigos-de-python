c = v1 = v2 = m = 0
M = r = ''
while True:
    print('-'*20)
    print('REGISTRO')
    print('-' * 20)
    n = str(input('Qual o nome do produto?')).strip().capitalize()
    p = int(input('Qual o preço do produto?R$'))
    if p > 1000:
        v2 += 1
    print('-' * 20)
    r = str(input('Você quer continuar?[S/N]')).strip().lower()
    while r not in 'sn':
        print('Essa opção é inválida. Tente novamente.')
        r = str(input('Você quer continuar?[S/N]')).strip().lower()
    c += 1
    if c == 1:
        m = p
        M = n
    else:
        if m > p:
            m = p
            M = n
    v1 += p
    if r == 'n':
        break
print(f'O produto com menor preço é {M} e custa R${m:.2f}')
print(f'Produtos custam mais de R$ 1000.00: {v2}')
print(f'O gasto total é de R${v1:.2f}')
