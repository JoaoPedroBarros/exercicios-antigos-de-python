a = int(input('Digite um número:'))
if a%4 == 0 and a%400 == 0 or a%100 != 0:
    print('Esse é um ano bissexto.')
else:
    print('Esse ano não é bissexto')
