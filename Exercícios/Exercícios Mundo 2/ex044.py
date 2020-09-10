f = float(input('Qual o valor inicial do produto:'))
print("""Condições de pagamento:
Dinheiro/Cheque
\033[31mÀ vista no cartão\033[m
\033[32m2x no cartão\033[m
\033[33m3x ou mais no cartão\033[m""")
o = str(input('Escolha uma opção de pagamento:'))
l = o.upper()
if l == 'DINHEIRO' or l == 'CHEQUE' or l == 'DINHEIRO/CHEQUE':
    print('O produto escolhido passa a custar {:.2f}'.format(f*0.9))
elif l == 'À VISTA NO CARTÃO':
    print('O produto escolhido passa a custar {:.2f}.'.format(f*0.95))
elif l == '2x NO CARTÃO':
    print('O produto escolhido passa a custar {:.2f}.'.format(f))
elif l == '3X OU MAIS NO CARTÃO':
    print('O produto escolhido passa a custar {:.2f}.'.format(f*1.2))
else:
    print('Não houve opção selecionada ou a opção teve um erro de digitação.')
