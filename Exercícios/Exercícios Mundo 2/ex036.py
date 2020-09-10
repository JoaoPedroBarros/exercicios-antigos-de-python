v = float(input('Qual o valor da casa? R$'))
s = float(input('Qual o seu salário? R$'))
t = float(input('Em quantos anos pretende pagar?'))*12
r = v/t
if r > (s*0.3):
    print('Você não atende as condições exigidas. O seu empréstimo foi negado.')
else:
    print('Você atende as condicões exigidas. O empréstimo será efetuado.')
#função end = ' ' (encerra a quebra de linha)