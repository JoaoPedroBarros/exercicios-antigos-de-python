p = int(input('Qual o primeiro termo da PA?'))
r = int(input('Qual a razão da PA?'))
c = int(input('Quantos termos você quer?'))
m = 1
e = 1
print(p, end=' ')
while m != c:
    e += 1
    m += 1
    p += r
    print(p, end=' ')
    if m == c:
        m = 0
        c = int(input('\nQuantos termos você quer?'))
if c == 0:
    print('O programa foi encerrado com {} termos mostrados.'.format(e))
