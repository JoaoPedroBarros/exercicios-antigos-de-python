f = float(input('Qual o valor inicial do produto:'))
print("""Condições de pagamento:
[ 1 ]Dinheiro/Cheque
[ 2 ]\033[31mÀ vista no cartão\033[m
[ 3 ]\033[32m2x no cartão\033[m
[ 4 ]\033[33m3x ou mais no cartão\033[m""")
o = int(input('Escolha uma opção de pagamento:'))
if o == 1:
    print('O produto escolhido passa a custar {:.2f}'.format(f*0.9))
elif o == 2:
    print('O produto escolhido passa a custar {:.2f}.'.format(f*0.95))
elif o == 3:
    print('O produto escolhido passa a custar {:.2f}.'.format(f))
elif o == 4:
    print('O produto escolhido passa a custar {:.2f}.'.format(f*1.2))
else:
    print('Não houve opção selecionada ou a opção teve um erro de digitação.')