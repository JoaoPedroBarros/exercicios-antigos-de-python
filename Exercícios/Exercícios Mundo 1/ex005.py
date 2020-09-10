k = int(input('Digite um número:'))
cor = {'a':'\033[4;37m', 'o':'\033[4;35m', 'p':'\033[4;31m','l':'\033[m'}
print('O antecessor de {}{}{} é {}{}{} \ne o seu sucessor é {}{}{}.'.format(cor['a'],k,cor['l'],cor['o'],k-1,cor['l'],cor['p'],k+1,cor['l']))
