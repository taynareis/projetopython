'''Crie um programa que simule um caixa eletronico. No inicio, pergunte ao usuario qual será o valor a ser sacado (inteiro)
e o programa vai informar quantas células de cada valor serão entregues. Considerando celulas de 50, 20, 10, 1.'''
print('=' * 30)
print('{:^30}'.format('BANCO DA TAY'))
print('=' * 30)
valor = int(input('Qual valor gostaria de sacar? R$ '))
montante = valor
cedula = 50
totalced = 0
while True:
    if montante >= cedula:
        montante -= cedula
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cédula(s) de R$ {cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalced = 0
        if montante == 0:
            break
print('=' * 30)
