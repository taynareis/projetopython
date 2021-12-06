'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.'''
print('=-=' * 6)
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    for c in range(1, 11):
        print('{} x {:2} = {}'.format(n, c, n * c))
    print('=-=' * 6)
print('PROGRAMA ENCERRADO!')