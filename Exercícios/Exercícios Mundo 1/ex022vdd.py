n = input('Qual o seu nome?')
u = n.upper()
l = n.lower()
p = n.split()
t = len(''.join(p))
q = len(p[0])
print("""Aqui está o seu nome em:
Letras Maíusculas - {}
Letras minúsculas - {}
Seu nome inteiro possui {} letras
Seu primeiro nome nome possui {} letras.""".format(u,l,t,q))
