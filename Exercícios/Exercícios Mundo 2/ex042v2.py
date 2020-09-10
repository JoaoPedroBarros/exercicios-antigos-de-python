r = float(input('Digite o tamanho da primeira linha?'))
s = float(input('Digite o tamanho da segunda linha?'))
t = float(input('Digite o tamanho da terceira linha?'))
if abs(r-t) < s < r+t:
    g = 'nome'
    if r != s != t != r:
        g = 'escaleno'
    if r == t != s or s == t != r or r == s != t:
        g = 'isósceles'
    if r == t == s:
        g = 'equilátero'
    print('Essas linhas podem formar um triângulo {}.'.format(g))
else:
    print('Essas linhas não podem formar um triângulo.')

# Ficou show
# ***'!=' não possui continuidade como o '='.***