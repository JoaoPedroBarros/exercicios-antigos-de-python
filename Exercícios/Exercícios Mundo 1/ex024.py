c = str(input('Em qual cidade você nasceu?'))
c.upper()
y = c.find('ANTÔNIO'or'ANTONIO')
if y == 0:
    print('A nome da sua cidade começa com Antônio')
else:
    print('O nome da sua cidade não começa com Antônio')
