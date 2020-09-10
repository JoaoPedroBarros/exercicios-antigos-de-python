f = float(input('Digite a primeira nota:'))
h = float(input('Digite a segunda nota:'))
m = (f+h)/2
if m >= 7.0:
    print('Você passou.')
elif m < 5.0:
    print('Você reprovou.')
elif 5.0 <= m < 7:
    print('Você está de recuperação.')
