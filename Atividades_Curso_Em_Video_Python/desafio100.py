'''Faça um programa que tenha uma lista chamada números e duas funções chamadas Sorteio e Somapar.
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda vai mostrar a soma entre
todos os valores pares sorteados na função anterior.'''
from random import randint
numeros = list()


def sorteio(num):
    for num in range(0, 5):
        num = randint(1, 20)
        numeros.append(num)
    print(f'Sorteando 5 valores da lista: {numeros}. Pronto!')


def somapar(num):
    soma = 0
    for num in numeros:
        if num % 2 == 0:
            soma += num
    print(f'Somando os valores pares de {numeros}, temos {soma}!')


sorteio(numeros)
somapar(numeros)
