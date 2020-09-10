from random import randint
from time import sleep
print('O computador escolheu um número entre 0 e 10 (0 e 10 não inclusos)')
sleep(2)
print('Tente adivinhá-lo')
d = randint(1, 9)
y = int(input('Qual o seu palpite:'))
c = 1
while d != y:
    c += 1
    if d > y:
        print('Mais... Tente novamente')
        y = int(input('Qual o seu próximo palpite?'))
    else:
        print('Menos... Tente novamente')
        y = int(input('Qual o seu próximo palpite?'))
print('Parabéns você acertou em {} palpites.'.format(c))
