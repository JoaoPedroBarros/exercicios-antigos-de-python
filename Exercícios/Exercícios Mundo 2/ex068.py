from time import sleep
from random import randint
print('-'*20)
print('Vamos jogar ímpar/par?')
print('-'*20)
sleep(1)
j = ''
d = c = e = 0
while True:
    e = randint(1, 10)
    j = str(input('Você quer par ou ímpar?')).lower()
    d = int(input('Quantos números você vai jogar?'))
    if j == 'impar' or j == 'ímpar':
        if (e+d) % 2 == 0:
            print(f'''O PC escolheu {e}. O total é {e + d}. Você perdeu!''')
            break
    elif j == 'par':
        if (e+d) % 2 != 0:
            print(f'''O PC escolheu {e}. O total é {e + d}. Você perdeu!''')
            break
    else:
        print('O comando digitado é inválido. Tente novamente.')
        j = str(input('Você quer par ou ímpar?')).lower()
    print(f'O PC escolheu {e}. O total é {e + d}. Você ganhou!')
    c += 1
print(f'Você conseguiu {c} vitória(s) consecutiva(s).')
