n = int(input('Digite um número:'))
p = '\033[4;33m'
i = '\033[m'
print('O {}Dobro{} desse número é {}.'.format(p,i,n*2))
print('O {}Triplo{} dele é {}'.format(p,i,n*3))
print('A sua {}Raiz quadrada{} é {:.2f}.'.format(p,i,n**(1/2)))
