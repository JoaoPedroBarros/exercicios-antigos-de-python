import random
y = ['Pedra', 'Papel', 'Tesoura']
f = random.choice(y)
print('='*20)
print('Vamos jogar Jokenpo?')
print('='*20)
u = str(input('Escolha entre Pedra, Papel ou Tesoura:'))
if f == u:
    print('Empatou. Eu escolhi o mesmo que você.')
elif f == 'Pedra' and u == 'Papel':
    print('Você ganhou! Eu escolhi Pedra.')
elif f == 'Papel' and u == 'Pedra':
    print('Você perdeu! Eu escolhi Papel.')
elif f == 'Tesoura' and u == 'Papel':
    print('Você perdeu! Eu escolhi Tesoura.')
elif f == 'Papel' and u == 'Tesoura':
    print('Você ganhou! Eu escolhi Papel.')
elif f == 'Tesoura' and u == 'Pedra':
    print('Você ganhou! Eu escolhi Tesoura.')
elif f == 'Pedra' and u == 'Tesoura':
    print('Você perdeu! Eu escolhi Pedra.')
