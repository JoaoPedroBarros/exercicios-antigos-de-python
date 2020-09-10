while True:
    t = int(input('Digite um número:'))
    if t < 0:
        print('Programa encerrado')
        break
    for c in range(1, 11):
        print(f'{t}X{c}={t*c}')
