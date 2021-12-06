'''Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem de analisar todos os valores e dizer qual deles é o maior.'''


def maior(* num):
    tam = len(num)
    print('=-' * 30)
    print('Analizando os valores passados...')
    if num == ():
        print('Foram informados 0 valores ao todo.')
    else:
        print(f'{num} Foram informados {tam} valores ao todo.')
        print(f'O maior valor informado foi {max(num)}')


maior(4, 5, 8, 10)
maior(9, 4, 18)
maior(6, 1)
maior(9)
maior()
