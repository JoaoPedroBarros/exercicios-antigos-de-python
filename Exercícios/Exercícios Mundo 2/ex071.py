q = int(input('Quanto você vai sacar?'))
c = q % 50
c1 = q//50
c2 = (q % 50)//20
c3 = (c % 20)//10
c4 = (c % 10)//1
print(f'Total de {c1} cédulas de R$50')
print(f'Total de {c2} cédulas de R$20')
print(f'Total de {c3} cédulas de R$10')
print(f'Total de {c4} cédulas de R$1')

# Funciona, mas foi feito sem nenhuma estrutura de comando
