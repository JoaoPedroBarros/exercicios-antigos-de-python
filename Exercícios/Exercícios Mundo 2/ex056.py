i = 0
p = 0
o = 0
m = ''
h = 0
s = 0
for a in range(1, 5):
    print('-'*3, 'Pessoa {}'.format(a), '-'*3)
    b = str(input('Qual o seu nome?')).strip()
    c = int(input('Qual a sua idade?'))
    d = str(input('Qual o seu sexo? [M/F]:')).lower().strip()
    i += c
    if a == 1:
        h = c
        m = b
    if c > h and d == 'm':
        h = c
        m = b
    if c < 20 and d == 'f':
        p += 1
    if d == 'm':
        s += 1
print('A média das idades é {}'.format(i/4))
if p == 0:
    print('Não há mulhere(s) com menos de 20 anos na lista acima')
else:
    print('Há {} mulhere(s) com menos de 20 anos'.format(p))
if s == 0:
    print('Não há homens na lista acima.')
else:
    print('O homem mais velho se chama {} e tem {}.'.format(m, h))
# in 'Mm' - esse comando inclui todas strings nas aspas