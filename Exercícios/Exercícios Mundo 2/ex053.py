f = str(input('Digite uma frase ou palavra:')).lower().strip()
r = f.replace(' ', '')
o = r[::-1]
print('O inverso de {} é {}.'.format(r, o))
if r == o:
    print('Essa frase/palavra é um palíndromo.')
else:
    print('Essa frase/palavra não é um palíndromo.')
