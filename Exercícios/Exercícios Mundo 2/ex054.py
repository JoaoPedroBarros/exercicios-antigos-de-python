from datetime import datetime
y = datetime.today().year
o = 0
h = 0
for a in range(1, 8):
    b = int(input('Em que ano você nasceu?'))
    m = y-b
    if m >= 18:
        o = o+1
    if m < 18:
        h = h+1
print('Dentre os escolhidos, há {} pessoas que alcançaram a maioridade'.format(o), end='')
print(' e há {} que ainda não a alcançaram.'.format(h))
