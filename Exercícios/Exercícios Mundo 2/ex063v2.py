print('='*3, 'Sequência de Fibonacci', '='*3)
e = int(input('Quantos termos você quer?'))
p = 0
s = 1
t = 0
c = 2
print(p, s, end=' ')
while c < e:
    t = p+s
    print(t, end=' ')
    p = s
    s = t
    c += 1
