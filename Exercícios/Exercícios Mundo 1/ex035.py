a = float(input('Qual o tamanho da primeira reta?'))
b = float(input('Qual o tamanho da segunda reta?'))
c = float(input('Qual o tamanho da terceira reta?'))
if abs(a-c)<b<(a+c):
    print("Essas retas podem formar um triângulo.")
else:
    print("Essas retas não podem formar um triângulo.")