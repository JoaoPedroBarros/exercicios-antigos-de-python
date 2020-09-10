c = float(input('Quantos reais você possui na carteira?'))
print('Com \033[32mR${:.2f}\033[m você pode comprar \033[34mU${:.2f}\033[m.'.format(c,c/3.27))
