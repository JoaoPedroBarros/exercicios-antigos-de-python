r = float(input('Digite o tamanho da primeira linha?'))
s = float(input('Digite o tamanho da segunda linha?'))
t = float(input('Digite o tamanho da terceira linha?'))
if abs(r-t) < s < r+t and r != s != t:
    print('Essas linhas podem formar um triângulo.')
    print('Esse triângulo é Escaleno')
elif abs(r - t) < s < r + t and r == s == t:
    print('Essas linhas podem formar um triângulo.')
    print('Esse triângulo é Equilátero.')
elif abs(r-t) < s < r+t and t == r != s or t == s != r or r == s != t:
    print('Essas linhas podem formar um triângulo.')
    print('Esse triângulo é Isósceles')
else:
    print('Essas linhas não podem formar um triângulo.')
