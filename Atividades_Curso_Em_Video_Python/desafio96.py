'''Faça um programa que tenha uma função chamada área(), que receba qs dimensões de um terreno retangular
(largura e comrpimento) e mostre a área do terreno'''


def area(a, b):
    terreno = a * b
    print(f'A area do terreno {a} X {b} é igual a {terreno}m²')


larg = float(input('Largura do terreno: '))
compr = float(input('Comprimento do terreno: '))
area(larg, compr)
