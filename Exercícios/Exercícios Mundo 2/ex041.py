e = int(input('Em que ano você nasceu?'))
q = 2020-e
if q < 9:
    print('Esse nadador é mirim.')
elif 9 <= q < 14:
    print('Esse nadador é mirim.')
elif 14 <= q < 19:
    print('Esse nadador é Junior.')
elif 19 <= q < 20:
    print('Esse nadador é Sênior.')
elif q >= 20:
    print('Esse nadador é Master.')
