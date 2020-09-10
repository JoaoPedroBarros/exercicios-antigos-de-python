from datetime import date
i = int(input('Em que ano você nasceu?'))
o = date.today().year
l = o - i
if l <= 9:
    print('Esse nadador é mirim.')
elif l <= 14:
    print('Esse nadador é infantil.')
elif l <= 19:
    print('Esse nadador é junior.')
elif l <= 25:
    print('Esse nadador é sênior.')
else:
    print('Esse nadador é master.')
