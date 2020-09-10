f = int(input('Digite o primeiro termo da PA:'))
r = int(input('Digite a razão da PA:'))
o = f
print(f, end=' → ')
for p in range(1,10):
    o = o + r
    print(o, end=' → ')
