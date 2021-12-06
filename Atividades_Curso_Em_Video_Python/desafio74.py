'''Crie um programa que vai gerar cinco numeros aleatorios e colocar em uma tupla. Depois disso, mostre a listagem
de numeros gerados e tambem indique o menor e o maior valor que estao na tupla.'''
from random import randint
sorteado = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Valores sorteados: {sorteado}')
print(f'Menor valor sorteado: {min(sorteado)}')
print(f'Maior valor sorteado: {max(sorteado)}')
