u = int(input('Digite um número:'))
print('1 - BINÁRIO, 2 - OCTAL, 3 - HEXADECIMAL')
i = int(input('Escolha um método de conversão acima:'))
if i == 1:
    print(bin(u)[2:])
elif i == 2:
    print(oct(u)[2:])
elif i == 3:
    print(hex(u)[2:])
else:
    print('O método selecionado não existe.')
