s = str(input('Qual o seu sexo?[M/F]')).strip().lower()[0]
while s not in 'mf':
    print('A opção não está disponível, selecione M ou F')
    s = str(input('Qual o seu sexo?[M/F]')).strip().lower()[0]
