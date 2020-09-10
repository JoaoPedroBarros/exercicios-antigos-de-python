# Modelo com o modulo "datetime"
import datetime
p = int(input('Em que ano você nasceu?'))
g = datetime.date.today().year
a = g-p
if a == 18:
    print('Você deve alistar!')
elif a > 18:
    print('Já passou o tempo do seu alistamento.', end='')
    print('O seu prazo expirou a {} anos.'.format(a-18))
    print('Você deveria ter ou se alistou em {}.'.format((p+18)))
elif a < 18:
    print('Você ainda deve se alistar.', end='')
    print('Faltam {} anos para o seu alistamento.'.format(18-a))
    print('Você deve se alistar em {}.'.format((p+18)))
