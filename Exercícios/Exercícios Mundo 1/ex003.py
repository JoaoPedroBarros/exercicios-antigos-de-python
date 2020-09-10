a = int(input('Digite um número:'))
b = int(input('Digite outro número:'))
cores = {'amarelo':'\033[1;33m','azul':'\033[1;34m','verde':'\033[1;36m','limpa':'\033[m'}
print("""A soma de {}{}{} + {}{}{} é {}{}{}.""".format(cores['amarelo'],a,cores['limpa'],cores['azul'],b,
cores['limpa'],cores['verde'],a+b,cores['limpa']))
