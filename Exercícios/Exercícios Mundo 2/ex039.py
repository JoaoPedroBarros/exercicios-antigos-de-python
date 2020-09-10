a = int(input('Em que ano você nasceu?'))
i = 2020-a
if i == 18:
    print('É hora de se alistar.')
elif i > 18:
    print('Você já passou do tempo de se alistar.')
    print('O seu prazo expirou há {} anos.'.format(i-18))
    print('Você deveria ou se alistou em {}.'.format(abs((i-18)-2020)))
elif i < 18:
    print('Você ainda vai se alistar.')
    print('Faltam {} anos para você se alistar.'.format(18-i))
    print('Você deve se alistar em {}.'.format(2020+(18-i)))
