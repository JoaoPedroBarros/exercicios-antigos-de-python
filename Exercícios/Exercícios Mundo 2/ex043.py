p = float(input('Digite seu peso, em Kg:'))
h = float(input('Digite a sua altura, em metros:'))
c = p/(h**2)
print('O seu IMC é {:.1f}.'.format(c))
if c < 18.5:
    print('Você está abaixo do peso ideal.')
elif 18.5 <= c < 25:
    print('Você está no peso ideal.')
elif 25 <= c < 30:
    print('Você está em obrepeso.')
elif 30 <= c <= 40:
    print('Você está obeso.')
elif c > 40:
    print('Você é um obeso mórbido.')
