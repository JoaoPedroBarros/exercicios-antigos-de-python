first = int(input('Digite um número:'))
ratio = int(input('Digite a razão:'))
dec = first + (10-1) * ratio
for c in range(first,dec+ratio,ratio):
    print(c, end='→')
