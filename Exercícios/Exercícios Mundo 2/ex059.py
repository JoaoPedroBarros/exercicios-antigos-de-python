p = int(input('Digite um número:'))
s = int(input('Digite outro número:'))
print('''[1]somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
[6] menu''')
c = int(input('Qual a operação escolhida?'))
while c != 5:
    if c == 1:
        print('A soma desses números é {}.'.format(p+s))
    if c == 2:
        print('A multiplicação desses números é {}.'.format(p*s))
    if c == 3:
        if p > s:
            print('O maior número é {}.'.format(p))
        elif s > p:
            print('O maior número é {}.'.format(s))
        else:
            print('Os dois números são iguais.')
    if c == 4:
        p = int(input('Digite um número:'))
        s = int(input('Digite outro número:'))
    if c == 6:
        print('''[1 ]somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
[6] menu''')
    if c > 6:
        print('Opção inválida. Escolha uma opções do menu.')
    c = int(input('Qual a próxima operção?'))
if c == 5:
    print('O programa foi encerrado.')

