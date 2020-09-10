print('='*3, 'Sequência de Fibonacci', '='*3)
e = int(input('Quantos termos você quer?'))
p = 0
s = 1
c = 0
t = p+s
while c != e:
    c += 1
    if c == 1:
        print(p,s, end=' ')
        c = 3
    else:
        p = s
        s = t
        t = p + s
    print(t, end=' ')
