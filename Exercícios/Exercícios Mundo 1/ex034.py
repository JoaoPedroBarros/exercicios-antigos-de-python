o = float(input('Qual o seu salário:'))
if o>=1250.0:
    print('O seu aumento será de {:.2f}'.format(o*0.10))
else:
    print('O seu aumento será de {:.2f}'.format(o * 0.15))