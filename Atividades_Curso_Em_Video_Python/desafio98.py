'''Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: ínicio, fim e passo e realize
a contagem. Seu programa tem que realizar três contagens através da função criada: a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2. C) uma contagem personalizada'''
from time import sleep


def contador(i, f, p):
    print('=-' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= p
        print('FIM')


contador(1, 10, 1)
contador(10, 0, 2)
print('=-' * 20)
print('Agora é sua vez de personalizar!')
ini = int(input('Ínicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)
