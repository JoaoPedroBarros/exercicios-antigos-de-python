c1 = c2 = c3 = 0
while True:
    print('-'*20)
    print('CADASTRO')
    print('-' * 20)
    i = int(input('Qual a sua idade?'))
    s = str(input('Qual o seu sexo?[M/F]')).strip().lower()
    while s not in 'mf':
        print('Opção inválida. Tente novamente.')
        s = str(input('Qual o seu sexo?[M/F]')).strip().lower()
    print('-' * 20)
    v = str(input('Você quer continuar?[S/N]')).strip().lower()
    while v not in 'sn':
        print('Opção inválida.')
        v = str(input('Você quer continuar?[S/N]')).strip().lower()
    if i > 18:
        c1 += 1
    elif s in 'm':
        c2 += 1
    if i < 20 and s == 'f':
        c3 += 1
    if v == 'n':
        break
print(f'{c1} pessoa(s) com mais de 18 anos foram cadastradas.')
print(f'{c2} homem(ns) foram cadastrados.')
print(f'{c3} mulhere(s) com menos de 20 anos foram cadastradas.')
